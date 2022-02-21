
from abc import ABC ,abstractmethod
import enum

class myExceptions(Exception):
    def __init__(self,message) -> None:
        super().__init__(message)
        self.message=message

    def __str__ (self):
        return f"Error Is :  {self.message} ......."    
# --------------------------------------------------------------------------------
def gradValidator(grad):
    if not isinstance(grad , float):
        raise myExceptions (" plese inter a number between 16 -20")
    elif grad < 16 :
        raise myExceptions("Grad Point Average should be more than 16 .. ")

def secoreValidator(secore):
    if not isinstance(secore , int):
        raise myExceptions (" plese inter a number between 0 to 100 ")
    elif not  100 >= secore >0  :
        raise myExceptions (" secore should be betwen 0 to 100 ")

def yearsOfWorkValidator(year):
    if not year >=  1 :
        raise myExceptions ("years of work is less than 1 year")

def rankValidator(rank):
    if not isinstance(rank ,str):
        raise myExceptions("you should type a-c carecter ...")        
# =================================================================================
class participant(ABC):
    def __init__(self,name , family , codeMeli , fieldOfStudy, address) -> None:
        super().__init__()
        self.name=name
        self.family=family
        self.codeMeli=codeMeli
        self.fieldOfStudy=fieldOfStudy
        self.address=address

    @abstractmethod
    def finalSecoreCalck(self):
        pass 
    @abstractmethod 
    def showInfo(self):
        pass

# =================================================================================
class freeParticipant(participant):
    def __init__(self, name, family, codeMeli, fieldOfStudy, address ,testSecore,interviewSecore) -> None:
        super().__init__(name, family, codeMeli, fieldOfStudy, address)
        self.__testSecore=testSecore
        self.__interviewSecore=interviewSecore
        self.finall=0

    def finalSecoreCalck(self):
        self.finall=(self.__testSecore + self.__interviewSecore)/2
        return self.finall 

    def showInfo(self):
        self.finalSecoreCalck()
        return f" deray participanter {self.name}\t{self.family}\nwhit code meli number : {self.codeMeli}\naddress: {self.address}\nin level {self.fieldOfStudy}\nyour finall secore is : {self.finall}"
# ====================================================================================================================================================================================================================
class   Elitestudent(participant) :
    def __init__(self, name, family, codeMeli, fieldOfStudy, address,averageDegry,univercituRank) -> None:
        super().__init__(name, family, codeMeli, fieldOfStudy, address)  
        self.__averageDegry=averageDegry 
        self.univercituRank=univercituRank
        self.finall=0

    class universityRank(enum.Enum):
        A=100
        B=80
        C=60
    class  GradePointAverage (enum.Enum):
        GradA=100  #  more 18.5
        GradB=80  #  more 17.5-18.5
        GradC=60  #  more 16-17.5

    def finalSecoreCalck(self):
        if self.__averageDegry > 18.5 and self.univercituRank == "a" or "A":
            self.finall=(self.universityRank.A.value + self.GradePointAverage.GradA.value)/2
        elif self.__averageDegry > 18.5  and self.univercituRank == "b" or "B":
            self.finall=(self.universityRank.B.value + self.GradePointAverage.GradA.value)/2
        elif self.__averageDegry > 18.5  and self.univercituRank == "c" or "C":
            self.finall=(self.universityRank.C.value + self.GradePointAverage.GradA.value)/2




        elif  18.5   > self.__averageDegry >= 17.5   and self.univercituRank == "a" or "A":
            self.finall=(self.universityRank.A.value + self.GradePointAverage.GradB.value)/2     
        elif 18.5   > self.__averageDegry >= 17.5  and self.univercituRank == "b" or "B":
            self.finall=(self.universityRank.B.value + self.GradePointAverage.GradB.value)/2      
        elif 18.5   > self.__averageDegry >= 17.5 and self.univercituRank == "c" or "C":
            self.finall=(self.universityRank.C.value + self.GradePointAverage.GradB.value)/2      



        elif  17.5  > self.__averageDegry >= 16 and self.univercituRank == "a" or "A":
            self.finall=(self.universityRank.A.value + self.GradePointAverage.GradC.value)/2
        elif 17.5  > self.__averageDegry >= 16 and self.univercituRank == "b" or "B":
            self.finall=(self.universityRank.B.value + self.GradePointAverage.GradC.value)/2
        elif 17.5  > self.__averageDegry >= 16 and self.univercituRank == "c" or "C":
            self.finall=(self.universityRank.C.value + self.GradePointAverage.GradC.value)/2
        return self.finall    

    def showInfo(self):
        self.finalSecoreCalck()
        return f" deray participanter {self.name}\t{self.family}\nwhit code meli number : {self.codeMeli}\naddress: {self.address}\nin level {self.fieldOfStudy}\nyour finall secore is : {self.finall}"
#=====================================================================================================================================================================================================================
class employee(participant):
    def __init__(self, name, family, codeMeli, fieldOfStudy, address,performance,yearsOfWork) -> None:
        super().__init__(name, family, codeMeli, fieldOfStudy, address) 
        self.__performance=performance
        self.__yearOfWork=yearsOfWork
        self.finall=0
    class performancDegre(enum.Enum):
        A=0.1
        B=0.2

    def finalSecoreCalck(self):
        if self.__yearOfWork >5 :
            self.finall=(self.__performance * self.performancDegre.A.value)+self.__performance
        else   : 
            self.finall=(self.__performance * self.performancDegre.B)+self.__performance

        return self.finall    


    def showInfo(self):
        self.finalSecoreCalck()
        return f" deray participanter {self.name}\t{self.family}\nwhit code meli number : {self.codeMeli}\naddress: {self.address}\nin level {self.fieldOfStudy}\nyour finall secore is : {self.finall}"


# =======================================================================================================
participantList=[]
participant1=freeParticipant("ali","rezaii","487717*","tajrobi","hbfhrejbgherbhre",100,100)
participant2=Elitestudent("ali","rezaii","487717*","tajrobi","hbfhrejbgherbhre",19,"A")
participant3=employee("ali","rezaii","487717*","tajrobi","hbfhrejbgherbhre",100,6)
participantList.append(participant1)
participantList.append(participant2)
participantList.append(participant3)

# comment=input("Do You Want Countine ?  y/n   ")
# while True:
#     if comment == "n":
#         break
#     num=input("which kind of participant do you want to submit? 1: freeParticipate  2: Elite student  3 : employee" )
#     if num =="1":
#         try :
#             name=input("Enter Name : ")
#             family=input("Enter Family : ")
#             code=input("Enter CodeMeli : ")
#             filed=input("Enter Filed Of Study : ")
#             address=input("Enter Address : ")
#             testsec=int(input("Enter test secore  : "))
#             secoreValidator(testsec)
#             intervowesc=int(input("Enter interview secore   : "))
#             secoreValidator(intervowesc)
#             participant1=freeParticipant(name,family,code,filed,address,testsec,intervowesc)
#             print(participant1.showInfo())
#             participantList.append(participant1)
#             comment=input("Do You Want Countine ?  y/n   ") 
#         except myExceptions as Error:
#             print(Error)    
# # ------------------------------------------------------------------------------------------------------------
#     elif num == "2"  : 
#         try:
#             name=input("Enter Name : ")
#             family=input("Enter Family : ")
#             code=input("Enter CodeMeli : ")
#             filed=input("Enter Filed Of Study : ")
#             address=input("Enter Address : ")
#             avg=float(input("Enter avarage   : "))
#             uniRank=input("Enter univercity Rank   A-C  : ")
#             gradValidator(avg)
#             rankValidator(uniRank)
#             participant1=Elitestudent(name,family,code,filed,address,avg,uniRank)
#             print(participant1.showInfo())
#             participantList.append(participant1)
#             comment=input("Do You Want Countine ?  y/n   ") 
#         except myExceptions as Error:
#             print(Error)
# # ------------------------------------------------------------------------------------------------------------
#     elif  num == "3" : 
#         try:
#             name=input("Enter Name : ")
#             family=input("Enter Family : ")
#             code=input("Enter CodeMeli : ")
#             filed=input("Enter Filed Of Study : ")
#             address=input("Enter Address : ")
#             performanc=int(input("Enter performanc secore : "))
#             years=int(input("Enter years of work  : "))
#             secoreValidator(performanc)
#             yearsOfWorkValidator(years)
#             participant1=employee(name,family,code,filed,address,performanc,years)
#             print(participant1.showInfo())
#             participantList.append(participant1)
#             comment=input("Do You Want Countine ?  y/n   ") 
#         except myExceptions as Error:
#             print(Error)
#==============================================================================
greateStudents=[]
for i in participantList :
    if i.finalSecoreCalck() > 90:
        greateStudents.append(i)
print(greateStudents)

for i in greateStudents:
    print(i.showInfo())      
# =============================================================================
    