#coding=utf8
import re
"""
match()对所定的字符串匹配指定数据，只匹配一次（从指定位置进行匹配）
search()对所定的字符串匹配指定数据，只匹配一次（从整个字符串中进行匹配）
findall（）匹配多次，返回值是一个匹配的列表
finditer（）匹配多次  返回值是一个迭代器
split()根据表达式进行支付分割 返回分割后的列表
sub（）字符替换
"""

intro = "my name is damu , my age is 3o years old! "

print re.match(r"my",intro)
print re.match(r"my",intro,27).group()
print re.match(r"my",intro).span()

print re.search(r"my",intro)
print re.search(r"my",intro).group()
print re.search(r"my",intro).span()

print re.finditer(r"my",intro)
for p in  re.finditer(r"my",intro):
    print p,p.group(),p.span()

print re.findall(r"my",intro)


print re.split(r"\s+",intro)

print re.split(r"m",intro)

print re.sub(r"m","$$",intro)