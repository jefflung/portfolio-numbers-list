#update numbers in a list

list=['One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten']

number=int(input("Please enter a number from 1 to 10:"))

while number < 1 or number >10:
    number=int(input("Please enter a number (from 1 to 10):"))

if number==1:
    print("One")
elif number==2:
    print("Two")
elif number==3:
    print("Three")
elif number==4:
    print("Four")
elif number==5:
    print("Five")
elif number==6:
    print("Six")
elif number==7:
    print("Seven")
elif number==8:
    print("Eight")
elif number==9:
    print("Nine")
elif number==10:
    print("Ten")

delete=int(input("Please enter a number (from 1 to 10) to be deleted from the list:"))

while delete<1 or delete>10:
    delete=int(input("Please enter a number (from 1 to 10) to be deleted from the list:"))

del list[delete-1]

print(list)