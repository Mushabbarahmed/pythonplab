num=[12,87,23,12,45,23,12,76,56]

new=[i for i in num if i%3==0]
print("the number divisible in list are: " ,new)

even =[ i for i in num if i%2==0  ]
print("the even number in list are: ",even)
square=[]
for i in even:
    square.append(i*i)
print("the square of even numbers are: " ,square)

var=0
for i in even:
    var+=i
print("the sum of even number are : ", var)

duplicate=[]
for i in num:
    if i in duplicate:
        continue
    else:
        duplicate.append(i)
print("list after removing duplicate are :", duplicate)


dictionary={"mushabbar ahmed":"28 nov 2002","hashim":"18 12 2007","mubashir ahmed":"29 6 1995","Virat Kohli": "5 November 1988", "Umesh Yadav": "25 October 1987", "Manish Pandey":
"10 September 1989", "Rohit Sharma": "30 April 1987", "Ravindra Jadeja": "6 December 1988", "Hardik Pandya": "11 October 1993"}
def birth(name):
    print(dictionary[name])
birth("mushabbar ahmed")
