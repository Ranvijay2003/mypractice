ar=[]
for i in range(5):
    ar.append(int(input("Enter a number : ")))
sum = 1    
for num in ar:
    print("Array Element =",num)
    sum = sum * num
print("Multiple =",sum)
