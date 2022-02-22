# we are going to select players with specefic conditions 
# ==========================================================================
# ---------------------- Exception handeling class --------------------------
class myException(Exception):
    def __init__(self, message) -> None:
        super().__init__(message)
        self.message=message

    def __str__(self) -> str:
        return "Error  : "+ self.message +"......."   
# ============================================================================
# ------------------------------- Player selection class ---------------------
class player_Selection:
    def __init__(self,player_code,age,weight,height):
        self.player_code=player_code
        self.age=age
        self.weight=weight
        self.height=height
# -------------------  int , float checker functions ---------------------------
    @staticmethod
    def integer_check(number): # This method checks if the number is integer or not.
        try:
            number=int(number)
            return number
        except:         
                print("number is not valid ")       
                number=input("Enter again  ") 
                player_Selection.integer_check(number) 

    @staticmethod
    def float_check(number):     #This method checks if the number is float or not.
        try:
            number=float(number)
            return number
        except:         
                print("Number is not valid")       
                number=input("Enter agian ") 
                player_Selection.float_check(number) 
# ---------------------- register Permitted method -----------------------------
    def register_validator(self):
        try :
            if 25 >= int(self.age) >=15 :
                if not  80 >= float(self.weight) >=60 :
                    raise myException("weight not in range  ")
                elif not 170 <= float(self.height) <=190:
                    raise myException("height not in range ")
                else: 
                    return True

            elif 35 >= int(self.age) >= 25 :
                if not  70 >= float(self.weight) >=50 :
                     raise myException("weight not in range  ")
                elif not 170 <= float(self.height) <=190:  
                    raise myException("height not in range ")
                else: 
                    return True
        
        except myException as error:
            print(error)
            raise myException("This person id not allowed to be register")
# -------------------------------- information printer function-----------------------
    def show_info(self):
        print("-"*100)
        print(f"plyer code : {self.player_code}\tAge : {self.age}\theight : {self.height}\tweight : {self.weight}  registerd ") 
# =====================================================================================================
registered_list=[]
code=1
# ---------------------------- input data section --------------------------------------------
while True:
    try:
        code=input("Enter code : ")
        code=player_Selection.integer_check(code)
        if code == 0:
            break
        age=input("Enter age : ")
        age=player_Selection.integer_check(age)
        weight=input("Enter weight : ")
        weight=player_Selection.float_check(weight)
        height=input("Enter height : ")
        height=player_Selection.float_check(height)
        player1=player_Selection(1,age,weight,height)
        if  player1.register_validator():
            registered_list.append(player1)
    except myException as error:
        print(error)    
# -------------------------- result -----------------------------------------------------------
for player in registered_list:
    player.show_info()
    

