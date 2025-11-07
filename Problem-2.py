class OddSeries:
    def __init__(self,a):
        self.a=a
    def generate(self):
        series=[]
        num=1
        for _ in range(self.a):
            series.append(num)
            num+=2
        return series
a=int(input("Enter a number:"))
obj=OddSeries(a)
result=obj.generate()
print(",".join(map(str,result)))