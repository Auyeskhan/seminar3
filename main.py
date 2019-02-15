from linked_class import LinkedClass
from myclass import MyClass

rauan = LinkedClass()
rauan.adding(MyClass('Auyeskhan', 'Kostanay', 'Teacher'))

ali = LinkedClass()
ali.adding(MyClass('John', 'London', 'Writer'))

aman = LinkedClass()
aman.adding(MyClass('Shamel', 'Kostanay', 'Student'))

#print(rauan.uni(ali))
print(ali.inter(aman))
print(rauan.subs(aman))
print(rauan.eq(ali))
 
for i in rauan:
      i.meth_1()
