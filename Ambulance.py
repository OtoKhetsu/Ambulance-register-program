#program for ambulance registrers
#info
import random

name = input("Enter name :")
lname = input("Enter lastname :")
age = input("Enter age :")
phonenum = input("Enter phone number :")
adress = input("Enter Adress : ")
work = input("Enter (operation,echoscopy,familydoc) :")
insurance = input("Does he/she has insurance (yes,no): ")
if work == "operation" :
    if insurance == "yes" :
        total = 5000*0.45
    else :
        total = 5000
elif work == "echoscopy" :
    if insurance == "yes" :
        total = 70*0.45
    else :
        total = 70
elif work == "familydoc" :
    total = 0 
amb_code = random.randint(1000,9999)
#end of info input
#Info Table
print("  ----------------------Information Table -------------------------")
print(f" |name : {name} {lname}                                          ")
print(f" |age : {age}                                                    ")
print(f" |phone number : {phonenum}                                      ")
print(f" |Adress : {adress}                                              ")
print(f" |what need : {work}                                             ")
print(f" |Code : {amb_code}                                              ")
print(f" |total :{total}                                                 ")
print("  ----------------------Information Table -------------------------")
#End of info Table