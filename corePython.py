import  re

re.findall(r'(?im)th[\w ]+',"""This is the first line,
                                    another line,
                                    that line, it's the best""")

print(re.findall(r'(?s)th.+',"""
                    The first line
                    the second line
the third line
                    """))


print(re.search(r'''(?x)
                    \((\d{3})\) #区号
                    [ ]         #空格
                    (\d{3})     #前缀
                    -           #横线
                    (\d{4})     #终点数字
''','(800) 555-1212').groups())


#result = re.findall(r'http://(\w+\.)*(\w+\.com)','http://google.com http://google.com.cn http://code.google.com')
#print(result)

result = re.search(r'\((?P<area1code>\d{3})\) (?P<prefix>\d{3})-(?P<postfix>\d{4})','(800) 555-1212' ).groupdict()
print(result)

result  = re.match(r'''(?x)
                  #match (800) 555-1212,save areacode,prefix,no.

                  #(800)
                  \((?P<areacode>\d{3})\)
                  # space
                  [ ]
                  #555
                  (?P<prefix>\d{3})
                  #-
                  -
                  #1212
                  (?P<no>\d{4})

                  #space
                  [ ]
                  #match 800-555-1212
                  (?P=areacode)-(?P=prefix)-(?P=no)

                  #space
                  [ ]
                  #match 18005551212
                  1(?P=areacode)(?P=prefix)(?P=no)

                  ''','(800) 555-1212 800-555-1212 18005551212')


print(bool(result))