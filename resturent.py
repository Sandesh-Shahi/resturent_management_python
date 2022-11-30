import tkinter
from tkinter import messagebox #alert box
from fpdf import FPDF # pdf generation
print("<--------------------Our Resturent Menu------------------------>")
print("")
def menu(): #this is main function
    try:  #exception ----------when error is occured
        name = str(input("Enter your Name: "))
        while True:
            total_bill = 0 #initially total bill is 0
            count_pdf = 0 #count for read bill and generate  pdf
    # MAIN MENU ------------------------------------>
            print("Main Menu---->Select Your Choice!!")
            print("1.VEG Items")
            print("2.Non-VEG Items")
            print("3.Display Bill")
            print("4.PDF generate")
            print("5.Exit")
            Choice = int(input("Enter Your Choice from Above Menu: "))  #Enter the choice for select menu
            if Choice == 1:
                print("\n")
                f = open('bill.txt', 'a')
                f.write("\n<-----------------------Veg Items BIll-----------------------------------_>\n") #bill.txt generation 
                f.close()
                while (True): #infinite loop 
                    print("{} You have selected VEG items ".format(name))
 # VEG MENU ----------------------VEG _MENU------------------///////////////
                    print("1.Paneer with Roti")
                    print("2.Rajma Rice ")
                    print("3.Veg Briyani(paneer)")
                    print("4.MAIN MENU")
                    print("5.Bill Generate")
                    print("6.Exit")
                    Choice = int(input("Enter your choice form Above menu: "))
                    if Choice == 1:#------------------------------------------------------This is for paneer 
                        print("{} You have selected Paneer With Roti".format(name))
                        paneer_price = 150
                        print("Price of paneer is Rs.{} per plate".format(
                            paneer_price))
                        Quantity = int(input("Enter the quantity in plate: "))                           
                        conf = input("Are you want to confirm order(y/n): ")
                        if conf == "y":
                            print("Your order is placed ")
                            total_bill = total_bill+paneer_price*Quantity
                            f = open('bill.txt', 'a')#-----------Bill generate for paneer f=open("bill.txt",'a'---append fonction is used )
                            f.write('''
                            {},  Your order is paneer with roti 
                            price per plate RS.--> {}
                            Quantity you have ordered {}
                                '''.format(name, paneer_price, Quantity))
                            f.close()

                            print(
                                "<------------------------------------------------------------------>")
                        else:
                            print("Your order is Cancelled")
                            print("Please try Again!!")
                    elif Choice == 2:
                        print("{} You have selected Rajma Rice".format(name))
                        rajma_price = 200
                        print("Price of rajma is Rs.{} per plate".format(rajma_price))
                        Quantity = int(input("Enter the quantity in plate: "))
                        conf = input("Are you want to confirm order(y/n): ")
                        if conf == "y":
                            print("Your order is placed ")
                            total_bill = total_bill+rajma_price*Quantity
                            f = open('bill.txt', 'a')
                            f.write('''
                            {}, Your order is Rajma 
                            price per plate RS.--> {}
                            Quantity you have ordered {}
                            '''.format(name, rajma_price, Quantity))
                            f.close()
                            print(
                                "<------------------------------------------------------------------>")
                        else:
                            print("Your order is Cancelled")
                            print("Please try Again!!")
                    elif Choice == 3:
                        print("{} You have selected Veg_Briyani ".format(name))
                        briyani_price = 80
                        print("Price of briyani is Rs.{} per plate".format(
                            briyani_price))
                        Quantity = int(input("Enter the quantity in plate: "))
                        conf = input("Are you want to confirm order(y/n): ")
                        if conf == "y":
                            print("Your order is placed ")
                            total_bill = total_bill+briyani_price*Quantity
                            f = open('bill.txt', 'a')
                            f.write('''
                            {}, Your order is veg_briyani 
                            price per plate RS. -->{}
                            Quantity you have ordered {}
                
                            '''.format(name, briyani_price, Quantity))
                            f.close()
                            print(
                     "<------------------------------------------------------------------>")
                        else:
                            print("Your order is Cancelled")
                            print("Please try Again!!")
                    elif Choice == 4:  # MAIN MENU------------------------------>>
                        print("You are redirect to Main Menu ")
                        f = open('bill.txt', 'a')
                        f.write(
                            "Your total  Bill for Veg-Items = {}".format(total_bill))
                        f.close()
                        break

# Total BILL GENERATION for VEG ITEMS ----------------------------------------------------------------------//////////////////////////////////////////////////////////
                    elif Choice == 5:
                        messagebox.showinfo("Bill", "Your bill is generated!!")
                        f = open('bill.txt', 'a')
                        f.write(
                            "Your total  Bill for Veg-Items = {}".format(total_bill))
                        f.close()
                        displaye = input(
                            "are  you want to display your bill(y/n): ")
                        if displaye == 'y':
                            f = open("bill.txt", "r")
                            content = f.readlines()
                            for i in content:
                                print(i)
                            f.close()
                        else:
                            pass
                        break
                    elif Choice == 6:
                        conf = input("Have you generate your PDF(y/n): ")
                        if conf == 'y':
                            print("You are Exit from the System!!")
                            exit()
                        else:
                            print("Please Generate your PDF first! ")
                            break
                    else:
                        print("Invalid Choice!!")
                        print("Plese Enter choice avaible in our Menu")

            elif Choice == 2:
                print("\n")
# NOV-----VEG ----Items menu ---------------------------------------------------------------------------->
                f = open("bill.txt", 'a')
                f.write("\n<--------------------------------Non-Veg Items Bill----------------------------->\n")
                f.close()
                while True:
                    print("{} You have selected Non_veg Menu ".format(name))

                    print("1.Briyani")
                    print("2.Chiken leg piece")
                    print("3.Roasted Chicken")
                    print("5.Bill generate")
                    print("6.Main Menu")
                    print("7.Exit")
                    Choice = int(input("Enter your choice form Above  menu: "))
                    if Choice == 1:
                        print("{} You have selected Briyani ".format(name))
                        Briyani_price = 120
                        print(
                            "Price of not-veg Briyani is {} per plate ".format(Briyani_price))
                        Quantity = int(input("Eter the quantity in plate: "))
                        conf = input("Are want to confirm your order(y/n): ")
                        if conf == "y":
                            print("Your order is placed !")
                            total_bill = total_bill+Briyani_price*Quantity
                            f = open('bill.txt', 'a')
                            f.write('''
                            {}, Your order is  Briyani
                            price per plate RS.--> {}
                            Quantity you have ordered {}
                         
                            '''.format(name, Briyani_price, Quantity, Quantity))
                            f.close()
                            print(
                                "<------------------------------------------------------------------>")
                        else:
                            print("Your order is cancelled ")
                            print("Please try again")
                    elif Choice == 2:

                        print("{} You have selected Chicken leg piece ".format(name))
                        chickenl_price = 50
                        print("Price of chiken leg is {} per piece ".format(
                            chickenl_price))
                        Quantity = int(input("Eter the quantity in plate: "))
                        conf = input("Are want to confirm your order(y/n): ")
                        if conf == "y":
                            print("Your order is placed !")
                            total_bill = total_bill+chickenl_price*Quantity
                            f = open('bill.txt', 'a')
                            f.write('''
                            {}, Your order is  chicken leg piece
                            price per plate RS.--> {}
                            Quantity you have ordered {}
                           
                            '''.format(name, chickenl_price, Quantity))
                            f.close()
                            print(
                                "<------------------------------------------------------------------>")
                        else:
                            print("Your order is cancelled ")
                            print("Please try again")
                    elif Choice == 3:

                        print("{} You have selected Roasted Chicken ".format(name))
                        chickenr_price = 250
                        print("Price of roasted  chiken  is {} per piece ".format(
                            chickenr_price))
                        Quantity = int(input("Eter the quantity in plate: "))
                        conf = input("Are want to confirm your order(y/n): ")
                        if conf == "y":
                            print("Your order is placed !")
                            total_bill = total_bill+chickenr_price*Quantity
                            f = open('bill.txt', 'a')
                            f.write('''
                                {}, Your order is  Rosted chicken
                                price per plate RS.--> {}
                                Quantity you have ordered {}          
                                '''.format(name, chickenr_price, Quantity))
                            f.close()
                            print(
                                "<------------------------------------------------------------------>")
                        else:
                            print("Your order is cancelled ")
                            print("Please try again")
# Total BILL GENERATION FOR NON_VEG ITEMS----------------------_/////////////////////////////////////////////////////////
                    elif Choice == 5:
                        messagebox.showinfo(
                            "Bill", "Your bill is generated! for NON_VEG ITEMS!")
                        f = open('bill.txt', 'a')
                        f.write(
                            "Your total Bill for Non-veg items = {}".format(total_bill))
                        f.close()
                        displaye = input(
                            "are  you want to display your bill(y/n): ")
                        if displaye == 'y':
                            f = open("bill.txt", "r")
                            content = f.readlines()
                            for i in content:
                                print(i)
                        else:
                            break
                        break
                    elif Choice == 6:  # MAIN MENU---------------------------------------->
                        print("You are Redirect to the  MAIN MENU!")
                        f = open('bill.txt', 'a')
                        f.write(
                            "Your total Bill for Non-veg items = {}".format(total_bill))
                        f.close()
                        break
                    elif Choice == 7:
                        conf = input(
                            "Are you want to display your bill(y/n): ")
                        if conf == 'y':
                            f = open("bill.txt", "r")
                            content = f.readlines()
                            for i in content:
                                print(i)
                                f.close()
                                f = open('bill.txt', 'r+')
                                f.truncate(0)
                        else:
                            conf = input("have you generate your PDF(y/n): ")
                            if conf == 'y':
                                print("You are Exit from the System!!")
                                exit()
                            else:
                                print("Please Generate your PDF first! ")
                                break
                    else:
                        print("Invalid Choice!!")
                        print("Plese Enter choice avaible in our Menu")
# BIll Display--------------------------------?>>>>/////////////
            elif Choice == 3:
                f = open("bill.txt", "r")
                content = f.readlines()
                for i in content:
                    print(i)
# PDF GENERATION _--------------------------?//////////////////////////////////
            elif Choice == 4:
                PDF = FPDF()
                PDF.add_page()
                PDF.set_font("Arial", size=21)
                f = open("bill.txt", "r")
                for i in f:
                    PDF.cell(200, 10, txt=i, ln=3, align='C')
                PDF.output("{}.pdf".format(name))
                print("Pdf file Successfully Generated")
                count_pdf = 1
                f = open('bill.txt', 'r+')
                f.truncate(0)

# EXIT FROM SYSTEM------------------------?////////////////////////////////////
            elif Choice == 5:

                conf = input("Have you order anything (y/n): ")
                if conf == 'y':
                    conf=input("Have you generate your bill pdf(y/n): ")
                    if conf=='y':
                        print("Your are exit from our system!!")
                        exit()
                    else:
                        print("Don't forgot to Generate your bill PDF")
                        continue
                else:
                    print("Your exit from Our System!!")
                    exit()

            else:
                print("Invalid Choice!!")
                print("Plese Enter choice avaible in our Menu")
    except:

        f = open('bill.txt', 'r+')
        f.truncate(0)
    finally:
        print("Thank you for visiting")


menu()
