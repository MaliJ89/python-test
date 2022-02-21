class price:
    def __init__(self,list,number) :
        self.list=list
        self.number=number



    def __add__(self,obj2):  # pluse an object to another object
        tempList=[]
        for i in range(0, len (self.list)):
            sum=self.list[i] + obj2.list[i]
            tempList.append(sum)
        return tempList    


    def __truediv__(self,obj2):  # divison an object to another object  by /
        tempList=[]
        for i in range(0, len (self.list)):
            div=self.list[i]/ obj2.number
            tempList.append(div)
        return tempList    


    def __div__(self,obj2):  # divison an object to another object by /
        tempList=[]
        for i in range(0, len (self.list)):
            div=self.list[i] / obj2.number
            tempList.append(div)
        return tempList    

    def __floordiv__(self,obj2):  # divison an object to another object by //
        tempList=[]
        for i in range(0, len (self.list)):
            div=self.list[i] // obj2.number
            tempList.append(div)
        return tempList    

    def __mod__(self,obj2):
        tempList=[]
        for i in range(0, len (self.list)):
            mod=self.list[i] % obj2.number
            tempList.append(mod)
        return tempList         







    def __sub__(self,obj2):   #Subtraction an object of another object
        tempList=[]
        for i in range(0, len (self.list)):
            sub=self.list[i]- obj2.list[i]
            tempList.append(sub)
        return tempList    


    def __mul__(self,obj2):  #Multiplication an object to another object
        tempList=[]
        for i in range(0, len (self.list)):
            mul=self.list[i] * obj2.number
            tempList.append(mul)
        return tempList    

    def __eq__(self,obj2):  #Multiplication an object to another object

        if not isinstance(obj2 , price):
            return "not same objects"
        return self.list == obj2.list and self.number == obj2.number


    def __pow__(self,obj2):
       return self.number ** obj2.number 

    def __and__(self,obj2):
        return self.number & obj2.number
    def __lt__(self,obj2): 
        pass


    def __str__(self):
        return self.number , self.list
#====================================================================== 
list1=[1,7,14,32,15,18,16,25,11]
list2=[2,51,36,87,12,6,14,77,8]

price1=price(list1,2)
price2=price(list2,4)
price3=price(list1,2)

print(100*"*")
price4=price1 + price2
print(price4)

print(100*"*")
price5= price1 / price2
print(price5)

print(100*"*")
price6= price1 // price2
print(price6)

print(100*"*")
price7= price1 % price2
print(price7)

print(100*"*")
price8= price2 - price1
print(price8)

print(100*"*")
price9= price2 * price1
print(price9)

print(100*"*")
price10= price2 == price1
print(price10)

print(100*"*")
price10= price2 ** price1
print(price10)

print(100*"*")
price11= price2 & price1
print(price11)


# ===============================================================================