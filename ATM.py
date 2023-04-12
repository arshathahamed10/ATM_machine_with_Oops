"""ATM simulator using OOP Python"""
import random
class ATM:
    user_name = "arshathahamed10"
    password = "arshath8220866@"
    balance = 20000
   
    def __init__(self,user_name,password) -> None:
        if(self.user_name==user_name and self.password==password):
            print("-------------LOGIN SUCCESSFULLY-------------")
            self.dashBoard(user_name)
        else:
            print("<-------LOGIN FAILED-------")
            print("Invalid Username or Password")
            
    def dashBoard(self,user_name):
        print(f"Welcome {user_name}\n")
        while(True):
            print("1.Balance\n2.Withdraw\n3.Deposit\n4.Exit")
            option=int(input("Enter your option : "))
            self.generateOTP()
            user_otp = int(input("Enter Your Otp : "))
            res = self.checkOTP(user_otp)
            if(not res):
                print("<-----Invalid OTP,Please try again later------>")
                continue
            if (option==1):
                self.userBalance()
            elif (option==2):
                self.userWithdraw()
            elif (option==3):
                self.userDeposit()
            elif (option==4):
                print("Thank you for using ATM simulator.")
                break
            else:
                print("Invalid Syntax")
    def userBalance(self):
        print(f"Your current balance is {self.balance} Rs")
    def userWithdraw(self):
        amount=int(input("Enter the amount to withdraw : "))
        if (amount>self.balance):
            print("Insufficient Balance")
            exceed=amount-self.balance
            print(f"You have {exceed} Rs lack of Money")
        else:
            self.balance=self.balance-amount
            print("Amount Withdrawn Successfully")
    def userDeposit(self):
        amount=int(input("Enter the amount to Deposit : "))
        self.balance=self.balance+amount
        print(f"Amount {amount} deposited Successfully")
    def generateOTP(self):
        self.otp=random.randrange(100000,999999)
        print(f"Your OTP is {self.otp}")
    def checkOTP(self,user_otp):
        if(self.otp==user_otp):
            return True
        else:
            return False
if __name__=="__main__":
    print("Welcome to ATM Simulator")
    user_name=input("Enter the username : ")
    password=input("Enter your Password : ")
    user=ATM(user_name,password)
