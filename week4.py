name = "j"

if len(name)< 3:
    print("Name must be at least 3 characters long")
elif len(name)> 50:
    print("Name can be a maximun of 50 characters long")
else:
    print("Name looks good")

name = 3 

if name < 3:
    print("name must be at least 3 character long")
else:
    print("name looks good")

a = 1
while (a < 10):
    print (a)
    a = a + 1

a = 1
while a < 10:
    print(a)
    a +=1

a = 1
while (a < 10 ):
    print(a)
    a = a + 1
    if a == 5:
        break
else:
    print("The loop has succesfully completed")

fruits = ["Banana", "Cherry", "Orange", "Mango", "Pineapple", "Apple",]
for a in fruits:
    print(a)
    if a == "Pineapple":
        break

fruits = ["Banana", "Cherry", "Orange", "Mango", "Pineapple", "Apple"]
for a in fruits:
    print(a)
else:
    print("The fruits are Nice!")

fruits = {"Cherry": 40, "Mango": 70, "Apple": 100}

for fruit in fruits:
    print(fruits, fruits[fruit])

