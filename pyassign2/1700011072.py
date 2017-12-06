from urllib.request import urlopen

def link(source,target,amount):#连接网址
    url1='http://cs1110.cs.cornell.edu/2016fa/a1server.php?'
    url2='from='+source.upper()+'&to='+target.upper()+'&amt='+amount
    url=url1+url2
    return url

def calculate(url):#引用汇率
    doc=urlopen(url)
    docstr=doc.read()
    doc.close()
    jstr=docstr.decode('ascii')
    return jstr

def amountto(result):#从引用结果中提取数字
    xi=result.find('"to"')
    i=xi+8
    while result[i]!=' ':
        i=i+1
    amount_to=float(result[xi+8:i])
    return amount_to
    
def exchange(source,target,amount):#得出结果
    url=link(source,target,amount)
    result=calculate(url)
    amount_to=amountto(result)
    return amount_to

def main():#定义主函数
    source=input()
    target=input()
    amount=input()
    amount_to=exchange(source,target,amount)
    print(amount_to)

    
#以下是测试程序
    
def test_link():
    assert(link('USD', 'EUR', '2.5') == 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5')
    
def test_calculate():
    assert(calculate('http://cs1110.cs.cornell.edu/2016fa/a1server.php?from=USD&to=EUR&amt=2.5') == '{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }')
    
def test_amountto():
    assert(amountto('{ "from" : "2.5 United States Dollars", "to" : "2.0952375 Euros", "success" : true, "error" : "" }') == 2.0952375)    

def test_exchange():
    assert(exchange('USD', 'EUR', '2.5') == 2.0952375)
    
def testall():
    test_link()
    test_calculate()
    test_amountto()
    test_exchange()
    print('Everything is ready.')
    

if __name__ == '__main__':
    main()
