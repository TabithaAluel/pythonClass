x=[100,110,120,140,150]
# for a in x :
#     a*a in x
#     print(a)

#     n=0
#     x=range(1,n) 
#     for i in x:
#      i%3==0 in x
#     print(i)

# x = [[1,2],[3,4],[5,6]]
# y=[1,2]+[3,4]+[5,6]
# print(y)

# x = ['a','b','a','e','d','b','c','e','f','g','h']
# y=x(set)
# print(y)

x=range(100,200)
for i in x:
    if i%7==0 in x:
       print("The number is divisible by 7".format(i))
    else:
        print("The number is not divisible by 7".format(i))
    
def greet(age):
    name='Eunice'
    year_of_birth=2021-age
    students = [{"age": 19, "name": "Eunice"}, {"age": 21, "name": "Agnes"}, 
 {"age": 18, "name": "Teresa"}, {"age": 22, "name": "Asha"}]


    for student in students:
     print('Hello {name}, you were born in {age}'.format(name,year_of_birth))
    greet()

