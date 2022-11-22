import dns.resolver

result1 = dns.resolver.resolve('ipg.pt', 'A')
result2 = dns.resolver.resolve('google.com', 'A')
result3 = dns.resolver.resolve('facebook.com', 'A')
list1=[result1,result2,result3]
count=0
for val1 in list1:
    count=count+1
    for ipval in val1:
        print('IP', val1,",", ipval.to_text(),count)

"""
result4 = dns.resolver.resolve('google.com', 'MX')
result5 = dns.resolver.resolve('ipg.pt', 'MX')
list2=[result4,result5]
for val2 in list2:
    for exdata in val2:
        print(' MX Record:', exdata.exchange.to_text())

result6 = dns.resolver.resolve('mail.hashnode.com', 'CNAME')
result7 = dns.resolver.resolve('mail.ipg.com', 'CNAME')
result8 = dns.resolver.resolve('mail.sapo.com', 'CNAME')
list3=[result6,result7,result8]
for val3 in list3:
    for cnameval in val3:
        print(' cname target address:', cnameval.target)
"""