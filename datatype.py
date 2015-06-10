#list
l = ['a','b',3]
#print l

#tuple, 不能修改內容 但是能修改list的內容
t = ([1,2],3,'a','b')
print t
t[0].append(3)
print t

#set
s1={1,1,'a','b','a'}
print s1
s2=set(['a','b','c','c'])
print s2
#and
print s1&s2
#or
print s1|s2
#xor
print s1^s2

#dictionaries
d1={1:'A',2:'b','a':'aaa','b':4}
print d1
d2=dict([(0,'zero'),('one',1)])
print d2a
