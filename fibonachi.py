class Fib:
    def __init__(self,end) -> None:
        self.a=0
        self.b=1
        self.end=end

    def __iter__(self):
        return self

    def __next__(self):
        self.a,self.b=self.b,(self.a+self.b)
        if self.a > self.end:
            raise StopIteration
        return self.a            

fib=Fib(5000)       

for item in fib:
    print(item,end="\t")
