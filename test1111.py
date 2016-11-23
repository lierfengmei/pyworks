import  re

#编译compile
re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')
#使用application
print(re_telephone.match('010-51214223').group())
print(re_telephone.match('010-8088').group())


re_email = re.compile(r'^(.+)(\@[\w]+.com)$')
print(re_email.match('someone@gmail.com').group())
print(re_email.match('bill.gates@microsoft.com').groups())

re_email_version2 = re.compile(r'^\<([a-zA-Z\s]+)\>\s?(.+\@[\w]+.[a-zA-Z]+)$')
print(re_email_version2.match('<Tom Paris> tom@voyager.org').groups())


t = '19:35:30'
m = re.match(r'^([0-1][0-9]|[0-9]|2[0-3])\:([0-9]|[0-5][0-9])\:([0-9]|[0-5][0-9])$',t)
print(m.groups())

print(re.match(r'^(\d+?)(0*)$','102300').groups())

s = 'This and that'
print(re.findall(r'(th\w+)\sand\s(th\w+)',s,re.I))
re.finditer(r'(th\w+)\sand\s(th\w+)',s,re.I)