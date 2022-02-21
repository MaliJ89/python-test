class countItemOfItrable:
    def __init__(self,data) -> None:
        self.data=data
        self.index=0


    def __iter__(self):
        n=len(self.data)
        print(f"lenght of data is {n}")    
        return self

    def __next__(self):

        if self.index >= len(self.data):
            print("i show you all items ")
            raise StopIteration
        n=self.data[self.index]
        self.index+=1
        return f"the item number {self.index} of {self.data} is {n}"
        
# ============================================================================

for i in countItemOfItrable("mehdi") :
    print(i)