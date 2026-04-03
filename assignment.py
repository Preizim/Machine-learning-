#exercise Write a program that prints numbers 1–10 using a loop
cum=1
while cum <11:
    print(cum)
    cum+=1
    
    #Create a function that returns the square of a number.
def sqr(num):
    return num*num
result=  sqr(10)
print(result)

#Create a dictionary storing:  Name. Age Course Then print the course.

data={
'Name': 'Alase Praise',
'Age': 15,
'Course': 'Computer Engineering'
}

print(data['Course'])

# Write a program that reads a file and prints its content.
file= open('pra.txt', 'w')
file.write('Life is good and we all know that, right?')
file.close()

with open('pra.txt', 'r') as file:
    print(file.read())
