x=int(input("Enter a number: "))
series=[]
for i in range(1,x+1,2):
    series.append(i)
if x%2==0 and series:
    series.pop()
print(",".join(map(str,series)))
