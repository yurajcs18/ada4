import timeit
start=timeit.timeit()
a = []

number = int(input("Please Enter the Total Number of Elements : "))
for i in range(number):
    value = int(input("Please enter the %d Element of List1 : " %i))
    a.append(value)
    
bubblesort()
for i in range(number -1):
    for j in range(number - i - 1):
        if(a[j] > a[j + 1]):
             temp = a[j]
             a[j] = a[j + 1]
             a[j + 1] = temp
             
             
selectionsort()           
for k in range(len(a)):
   min_= k
   for l in range(k+1, len(a)):
      if a[min_] > a[l]:
         min_ = l
   
a[k], a[min_] = a[min_], a[k]

for k in range(len(a)):
   print(a[k])
   switch(p)
   case 1
   bubblesort()
   break
   case 2
   selectionsort()
   break
print("the list in ascending order is",a)

end=timeit.timeit()
print("the elapsed time is",end-start) 
