import pandas as pd
from pandas.core.frame import DataFrame

print("""***************************• Movies Ticket Booking System •***************************""")
global total_price

total_price = {"Movie Fee" : 10, "Seating Fee" : 0, "Ticket Fee" : 0 }

#funtion to get the user details........

def userdetail():
  print("""                -----------------×××××• Log In •×××××-----------------""")
  global username
  global usermail
  username = input("Name:_____")
  usermail = input("Email:_____")
  print("""\n_____________________________***** Welcome to Cinema *****_____________________________""")
userdetail()

#function for taking the payment from user........

def payment_meth():
  global payment
  global card_no
  global cvv_no
  global card_holder
  global bank
  print("\nSelect a Payment Method: \n 1)Cash\n 2)Credit/Debit Card\n 3)UPI\n 4)Net Banking ")
  payment = input("""\nEnter the payment method you want to use? \n»» """)
  if payment == "1":
    payment = "Cash"
    print("You have selected " + payment)
  elif payment == "2":
    payment = "Credit/Debit Card"
    print("You have selected " + payment)
    card_holder = input("""\nCard Holder's Name:_____""")
    card_no = input("""Card Number:_____""")
    cvv_no = input("""CVV:_____""")
  elif payment == "3":
    payment = "UPI"
    print("You have selected " + payment)
    print("""\nPlease pay us on:\n»»UPI ID: cineplex@upi.co««""")
  elif payment  == "4":
    payment = "Net Banking"
    print("You have selected "+ payment )
    print("\nSelect your particular bank: \n 1)SBI\n 2)HDFC\n 3)IDFC\n 4)ICICI\n 5)Kotak Mahindra")
    bank = input("""\nEnter the bank of your interest? \n»» """)
    if bank == "1":
      bank = "SBI"
    elif bank == "2":
      bank = "HDFC"
    elif bank == "3":
      bank = "IDFC"
    elif bank == "4":
      bank = "ICICI"
    elif bank == "5":
      bank = "Kotak Mahindra"
    payment = payment + " - " + bank
    print(payment)
  else:
    print("Invalid")
    payment_meth()
  print("""\n-------------------------------×××××• INVOICE •×××××-------------------------------""")
  print("""Name: """ + username + """                                     Email: """ + usermail)
  print("""\n1)Movie: """ + usermovie + """ \n2)Date: """ + userdate + """ \n3)Time: """ + usertime + """ \n4)Seat: """ + userseat) 
  print("\n",DataFrame) 
  print("""-----------------------------------------------------------------------------------""")
       
#function for booking the ticket......

def book_ticket():
  global location
  global userloc
  global usermovie
  global userdate
  global usertime
  global userseat
  global restart
  global confirmation
  global no_of_tickets
   
  print()
  print("Select a Location: \n 1)Damoh\n 2)Jabalpur\n 3)Sagour\n 4)Indore\n 5)Gwalior")
  location= input ("""\nEnter your location? \n»» """)
  if location == "1":
    userloc = "Damoh"
    print("\nYou have selected ",userloc)
    print("Available Movies in ",userloc)
    print("\nSelect a Movie: \n 1)Animal\n 2)Dunki\n 3)Salaar Part (One): Ceasefire")
    usermovie = input ("""\nEnter the movie you wanna watch? \n»» """)
    if usermovie == "1":
      usermovie = "Animal"
    elif usermovie == "2":
      usermovie = "Dunki"
    elif usermovie == "3":
      usermovie = "Salaar Part (One): Ceasefire"
    else:
      print("Invalid")
      restart = input("\nDo you want to restart? (Yes/No) \n»» ")
      if restart in ["Yes", "yes", "YES"]:
        book_ticket()
      elif restart in ["No", "no", "NO"]:
        print("\nThank you for using our services...... Have a nice day!")
      else:
        return
        
    print("You have selected ",usermovie)
    
    print("""\nSelect a Date: \n 1)Nov, 1 2024\n 2)Nov, 2 2024\n 3)Nov, 3 2024\n 4)Nov, 4 2024\n 5)Nov, 5 2024\n 6)Nov, 6 2024\n 7)Nov, 7 2024""")
    userdate = input ("""\nEnter the date on which you want to watch """ + usermovie + """? \n»» """)
    if userdate in ["1", "2", "3", "4", "5", "6", "7"]:
      userdate = "Nov, " + userdate + " 2024"
    else:
      print("Invalid")
      restart = input("\nDo you want to restart? (Yes/No) \n»» ")
      if restart in ["Yes", "yes", "YES"]:
        book_ticket()
      elif restart in ["No", "no", "NO"]:
        print("\nThank you for using our services...... Have a nice day!")
      else:
        return
        
    print("You have selected ",userdate)
    
    print("""\nSelect a Time: \n 1)10:00 AM\n 2)02:00 PM\n 3)06:00 PM""")
    usertime = input ("""\nEnter the time on which you want to watch """ + usermovie + """? \n»» """)
    if usertime == "1":
      usertime = "10:00 AM"
    elif usertime == "2":
      usertime = "02:00 PM"
    elif usertime == "3":
      usertime = "06:00 PM"
    else:
      print("Invalid")
      restart = input("\nDo you want to restart? (Yes/No) \n»» ")
      if restart in ["Yes", "yes", "YES"]:
        book_ticket()
      elif restart in ["No", "no", "NO"]:
        print("\nThank you for using our services...... Have a nice day!")
      else:
        return
        
    print("You have selected ",usertime)
    
    print("""\nSelect a Seat: \n 1)Orchestra (Price: +250)\n 2)Mezzanine (Price: +500)\n 3)Balcony (Price: +1000)\n 4)Random Seat (Price: +150)""")
    print(" Note: Seat will be assigned randomly in selected sections.")
    userseat = input ("""\nEnter the type of seat you want to book? \n»» """)
    if userseat == "1":
      userseat = "Orchestra"
      total_price["Seating Fee"] = 250
    elif userseat == "2":
      userseat = "Mezzanine"
      total_price["Seating Fee"] = 500
    elif userseat == "3":
      userseat = "Balcony"
      total_price["Seating Fee"] = 1000
    elif userseat == "4":
      userseat = "Random Seat"
      total_price["Seating Fee"] = 150
    else:
      print("Invalid ")
      restart = input("\nDo you want to restart? (Yes/No) \n»» ")
      if restart in ["Yes", "yes", "YES"]:
        book_ticket()
      elif restart in ["No", "no", "NO"]:
        print("\nThank you for using our services...... Have a nice day!")
      else:
        return 
        
    print("You have selected ",userseat)

    no_of_tickets = int(input("\nHow many tickets do you want to book? \n»» "))
    if no_of_tickets > 1:
      for i in range(no_of_tickets):
        total_price["Ticket Fee"] = total_price["Ticket Fee"] + 10
 
      total_price["Seating Fee"] = total_price["Seating Fee"] * no_of_tickets
    else:
      total_price["Ticket Fee"] = 10
        
    print("""You have chosen to book """ + str(no_of_tickets) + """ tickets""")

    global price , DataFrame
    price = {"Service" : ["Movie:", "Seating:", "Tickets:", "Total Price:"], "Charges" : [total_price["Movie Fee"], total_price["Seating Fee"], total_price["Ticket Fee"], str(float(total_price["Movie Fee"] + total_price["Seating Fee"] + total_price["Ticket Fee"])) ]}
    DataFrame = pd.DataFrame(price, index = ["1)","2)","3)","»»"])
    
    confirmation = input("""\nDo you want to confirm your booking? (Yes/No) \n»» """)
    if confirmation in ["Yes", "yes", "YES"]:
      print("Thank you ", username , ",for confirmation.")
      print("""\n-------------------------------------• Booking Information •-------------------------------------""")
      print("""1)Movie: """ + usermovie + """ \n2)Date: """ + userdate + """ \n3)Time: """ + usertime + """ \n4)Seat: """ + userseat) 
      print("\n",DataFrame) 
      print("""---------------------------------------------------------------------------------------------""")
     
      payment_meth()
      print("\nYour ticket is being processed......")
      print(username + ", your booking is confirmed.")
      print("""\nThank you for using our services...... Have a great movie experience!""")
    elif confirmation in ["No", "no", "NO"]:
      restart = input("\nDo you want to restart? (Yes/No) \n»» ")
      if restart in ["Yes", "yes", "YES"]:
        book_ticket()
      elif restart in ["No", "no", "NO"]:
        print("\nThank you for using our services...... Have a nice day!")
      else:
        return 
  else:
    print()
    print("""We're expanding..... Coming Soon!""")


print("""                   -----------------Select an option----------------""")
print(""" 1) Book Tickets\n 2) Order Snacks(on your seat)\n 3) Exit""")
option = input("»» ")
if option == "1":
  book_ticket()
elif option == "2":
  print("\nComing Soon!(sooner than you think)")
elif option == "3":
  print("\nThank you for using our services...... Have a nice day!")
else:
  print("\nInvalid")




