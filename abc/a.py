import re
s ='abcdegfhi'
pattern = r'(ab)cd(?P<pig>ef)'
#---------------------------------
# pattern = r'(\w):(\d+)'
# l = re.findall(pattern,s)
#-----------------------------
a = re.search(pattern,s)


print(a.pos)
print(a.endpos)
