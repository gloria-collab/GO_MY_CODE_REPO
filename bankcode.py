

'''Write a program that allows customers to:
1. Create an account with the account number generated if they do not have an account. All generated account numbers should begin with 0
2. Log in to the program if they have an account
3. Deposit money
4. Withdraw money from the account if they have a sufficient amount.
5. Users should be able to transfer money to other users in the account
6. Users should be able to check their account balances.
The program should keep running until the user decides to make it log out and/or quit.
The account data should be stored in a dictionary that looks like that below and kept in a file for persistent storage'''
import random


print("Welcome to The George's Bank ")
print("The passion of banking")

data= {}


number="0123456789"
whole="0"
string= whole + number
length= 10
account= "".join(random.sample(string, length))
account_num= whole + account



program = False

import ast

with open("databasecodes.txt", "r") as in_put:
    contents = in_put.read()
while not program:
    start= input("Do You Have An Account? \nYES/NO: ").lower()
    if start == "yes":
        account =str(input("Give Your Account Number: "))
        if account in data.keys():
            print ("welcome", data[account]["first_name"], data[account]["second_name"])
            login_pin=input("Enter Your login pin: ")
            print("Dear user, Do Well To Remember your login pin ")
            if login_pin == data[account]["login_pin"]: 
                options= int(input("what service would you like?\n1. Withdrawal \n2. Deposit \n3. Check balance\n4. Transfer\n>>>>"))
                choice = [1,2,3,4]

                if options in choice:
                    pin = data[account]["transaction_pin"]
                    if options == 1:
                        log= input("Enter transaction pin: ")
                        if log == pin:
                            withdraw_1= int(input("Enter amount to be withdrawn: "))
                            balan_ = data[account]["balance"]
                            if withdraw_1 > balan_:
                                print("Insufficient balance")
                                print("You have {} remaining".format(balan_))
                                continue_OH = int(input("Do you wish to:\n.1. back menu \n2. log out"))
                                
                            else:
                                data[account]["balance"]-= withdraw_1
                                print("You have been debited {}".format(withdraw_1))
                                print("Your New Balance is $", data[account]['balance'])
                                

                        else:
                            print("incorrect pin")
                            

                    elif options == 2:
                        log= input("Enter Transaction Pin: ")
                        if log == pin:
                            depo_= int(input("Enter amount: "))
                            data[account]["balance"]+= depo_
                            print("Current balance is ${}".format(data[account]["balance"]))
                            # continue1()/
                        else:
                            print("Incorrect pin")
                            

                    elif options == 3:
                        log= input("Enter transaction pin: ")
                        custom_fee= 50
                        if log == pin:
                            data[account]["balance"]-= custom_fee
                            print("$", data[account]["balance"])
                            
                        else:
                            print("Incorrect pin")
                            


                    elif options == 4:
                        user= input("Enter User Account Number: ")
                        if user in data:
                            amount= int(input("Enter Amount: $ "))
                            log= input("Enter Transaction Pin: ")
                            if log== pin:
                                data[user]["balance"]+= amount
                                data[account]["balance"]-=amount
                                print('$',amount, 'Has Been Transferred to',user, data[user]["first_name"], data[user]["second_name"])
                                
                            else:
                                print("incorrect pin")
                                
                        else:
                            print("user not found")
                            
                else:
                    print("invalid input")
                    break
                    

                with open("databasecodes.txt", "w") as in_put:
                    in_put.write(str(data))


            else: 
                print("incorrect pin") 
                


        else:
            print("user not found")
            break
            
    
    
    elif start == "no":
        intro = account_num
        print("Your issued account number: ", intro)
        if intro not in data:
            print("Your Account number is {}, keep for future use".format(intro))
            data.update({f'{intro}': {"first_name": " ",
                                    "second_name": " ",
                                    "login_pin": " ",
                                    "transaction_pin": " ",
                                    "balance": 30000
                                      }})
            info = input("State your first_name: ").capitalize()
            data[intro]["first_name"]= info
            info2= input("State your second_name: ").capitalize()
            data[intro]['second_name']= info2
            info3= input('Enter 4 digits\ntransaction acct: ')
            data[intro]["transaction_pin"]= info3
            info4= input("Enter 4 digits\nSet login pin: ")
            data[intro]["login_pin"]=info4




            print("Dear {} {}, Your Account Has Been Succesfully Created".format(info, info2))
            print("Welcome To The George's Bank")
            print("Thank You For Banking with Us")
            with open("databasecodes.txt", "w") as in_put:
                in_put.write(str(data))

    else:
        print("Invalid input")


    continue_OH = int(input("Do you wish to:\n1. back menu \n2. log out\n"))
    if continue_OH == 1:
        continue

    elif continue_OH == 2:
        print("Thank You For Banking With The George's ")
        print("Till Next Time")
        break
    else:
        print("Invalid input")
        print("Bye For Now")
        break

program= True

