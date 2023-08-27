import mysql.connector as sql

mycon = sql.connect(host='127.0.0.1', user='root', passwd='', database = 'bank_app')

mycursor = mycon.cursor()

# mycursor.execute("CREATE DATABASE bank_app")

# mycursor.execute("SHOW DATABASES")
# for db in mycursor:
#      print(db)

# mycursor.execute("CREATE TABLE customer_table(id INT(3) PRIMARY KEY AUTO_INCREMENT, fullname VARCHAR(50), email VARCHAR(50) UNIQUE, phone_number VARCHAR(11) UNIQUE, bvn VARCHAR (11) UNIQUE, username VARCHAR(50), password VARCHAR(50), account_no VARCHAR(10) UNIQUE, account_bal FLOAT(9) )")

# mycursor.execute("SHOW TABLES")
# for db in mycursor:
#     print(db)

# mycursor.execute('DROP TABLE transaction_table')

# mycursor.execute("ALTER TABLE transaction_table ADD time VARCHAR(7)")

# mycursor.execute("ALTER TABLE customer_tble CHANGE id customer_id INT(3) AUTO_INCREMENT")

# mycursor.execute("ALTER TABLE customer_tble ADD username VARCHAR(50) UNIQUE")
# mycursor.execute("ALTER TABLE customer_tble ADD password VARCHAR(50)")

# query = "INSERT INTO customer_tble(fullname, email, phone_number, bvn, username, password, account_no, account_bal) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
# val = (fullname, email, phone_number, bvn, username, password, account_no, account_bal)
# mycursor.execute(query, val)
# mycon.commit()
# print(mycursor.rowcount, 'row inserted successfully')

# mycursor.execute("CREATE TABLE transaction_table(transaction_id INT(3) PRIMARY KEY AUTO_INCREMENT, transaction_type VARCHAR(50), username VARCHAR(50) UNIQUE, amount FLOAT(9) UNIQUE, beneficiary VARCHAR(50), date_time VARCHAR(10) )")

# query = "INSERT INTO transaction_table(transaction_id, transaction_type, username, amount, beneficiary, date_time) VALUES(%s,%s,%s,%s,%s,%s)"
# val = (transaction_id, transaction_type, username, amount, beneficiary, date_time)
# mycursor.execute(query, val)
# mycon.commit()
# print(mycursor.rowcount, 'row inserted successfully')

# mycursor.execute("CREATE TABLE number_registration(id INT(3) PRIMARY KEY AUTO_INCREMENT, mtn_number INT(11), airtel_number INT(11), glo_number INT(11), etisalat_number INT(11) )")

# query = "INSERT INTO transaction_table(id, mtn_number, airtel_number, glo_number, etisalat_number) VALUES(%s,%s,%s,%s,%s)"
# val = (id, mtn_number, airtel_number, glo_number, etisalat_number)
# mycursor.execute(query, val)
# mycon.commit()
# print(mycursor.rowcount, 'row inserted successfully')

# query = ('DELETE FROM customer_table WHERE id =%s ')
# val = (10,)
# mycursor.execute(query,val)
# mycon.commit()
# mycursor.execute('DROP TABLE transaction_table')



import random
import time
import sys
import datetime as dt
class Page:
    def __init__(self, name):
        self.name = name
        self.main()

    def main(self):
        self.page1()

    def page1(self):
        time.sleep(1)
        print(f'''
        
                                                                    Welcome to {self.name} mobile bank application
        ''')
        time.sleep(2)
        print("""
                                                                                    1. Log in
                                                                                    2. Sign up
                                                                                    3. Help
                                                                                    4. Exit
        """)

        user = input("\nUser: ")
        if user == "1":
            self.log_in()
        elif user == "2":
            self.sign_up()
        elif user == "3":
            self.help1()
        elif user == "4":
            self.exit()
        while user != "1" "2" "3" "4":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nUser: ')
            if user == "1":
                self.log_in()
            elif user == "2":
                self.sign_up()
            elif user == "3":
                self.help1()
            elif user == "4":
                self.exit()



                                                # SIGN UP


    def sign_up(self):
        query = "INSERT INTO customer_table(fullname, email, phone_number, bvn, username, password, account_no, account_bal) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
        time.sleep(1)
        print('''
                                                                                    Sign up page
        ''')
        self.fullname = input(f"\nFullname: ")
        time.sleep(1)
        self.email_address = input("\nEmail address: ")
        time.sleep(1)
        self.phone_number = input("\nPhone number: ")
        time.sleep(1)
        self.bvn = random.randint(22000000000, 22999999999)
        print(f"\nYour BVN number is {self.bvn}")
        time.sleep(1)
        self.username = input("\nUsername: ")
        time.sleep(1)
        self.password = input(f"\nPassword: ")
        time.sleep(1)
        self.account_no = random.randint(2100000000, 2199999999)
        print(f"\nYour account number is {self. account_no}")
        time.sleep(1)
        self.account_bal = 0.00
        time.sleep(1)
        val = (self.fullname, self.email_address, self.phone_number, self.bvn, self.username, self.password, self.account_no, self.account_bal)
        mycursor.execute(query, val)
        mycon.commit()
        # print(mycursor.rowcount, 'row inserted successfully')
        print('\nPlease wait...')
        time.sleep(2)
        print("\nLoading...")
        time.sleep(3)
        print("\nSuccessfully registered")
        self.log_in()

                                                    
                                                    
                                                    
                                                    
                                                    # Log in


    
    def log_in(self):
        query = "SELECT username, password FROM customer_table WHERE username = %s AND password = %s"
        time.sleep(1)
        print('''
                                                                                    Log in page
        ''')
        self.username = input("\nUsername: ")
        time.sleep(1)
        self.password = input(f"\nPassword: ")
        time.sleep(1)
        val = (self.username, self.password)
        mycursor.execute(query, val)
        output = mycursor.fetchall()
        if output:
            print('\nPlease wait...')
            time.sleep(1.5)
            print("\nLoading...")
            time.sleep(2)
            self.home_page()
        else:
            print(f"\nWrong password or username!")
            user = input("\nPress 'a' to reset password or 'b' to sign up: ")


                                
                                
                                
                                
                                                    # For password


            
            time.sleep(1)
            print("""
                                                                                    Reset Password
            """)                    

            if user.lower() == "a":
                time.sleep(1)
                email = input("\nEnter your Email: ")
                time.sleep(1)
                query1 = ("SELECT email, password FROM customer_table WHERE email=%s")
                val1 = (email,)
                mycursor.execute(query1, val1)
                detail = mycursor.fetchall()

                if detail:
                    self.password = input("\nEnter your new password: ")
                    time.sleep(1)
                    self.confirm_password = input("\nConfirm your new password: ")
                    query = 'UPDATE customer_table SET password = %s WHERE email = %s'
                    val =(self.confirm_password, email)
                    mycursor.execute(query,val)
                    mycon.commit()
                    time.sleep(1)
                    print("\nPassword reset successfully.")
                    self.log_in()
                    if self.password != self.confirm_password:
                        print("\nPassword does not match!")
                        password = input("\nEnter your new password: ")
                        confirm_password = input("\nConfirm your new password: ")
                        query = 'UPDATE customer_table SET password = %s WHERE email = %s'
                        val =(confirm_password, email)
                        mycursor.execute(query,val)
                        mycon.commit()
                        time.sleep(1)
                        print("\nPassword reset successfully.")
                        self.log_in()
                else:
                    time.sleep(1)
                    print('\nWrong email address')
                    self.log_in()

                                    # For username

            # elif user.lower() == "b":
            #     time.sleep(1)
            #     email = input("\nEnter your Email: ")
            #     time.sleep(1)
            #     query1 = ("SELECT email, username FROM customer_table WHERE email=%s")
            #     val1 = (email,)
            #     mycursor.execute(query1, val1)
            #     detail = mycursor.fetchall()

            #     if detail:
            #         user_name = input("\nEnter your new username: ")
            #         time.sleep(1)
            #         confirm_username = input("\nConfirm your new username: ")
            #         query = 'UPDATE customer_table SET username = %s WHERE email = %s'
            #         val =(confirm_username, email)
            #         mycursor.execute(query,val)
            #         mycon.commit()
            #         time.sleep(1)
            #         print("\nUsername change successfully.")
            #         self.sign_in()
            #         if user_name != confirm_username:
            #             print("\nUsername does not match!")
            #             user_name = input("\nEnter your new username: ")
            #             time.sleep(1)
            #             confirm_username = input("\nConfirm your new username: ")
            #             query = 'UPDATE customer_table SET username = %s WHERE email = %s'
            #             val =(confirm_username, email)
            #             mycursor.execute(query,val)
            #             mycon.commit()
            #             time.sleep(1)
            #             print("\nUsername change successfully.")
            #             self.sign_in()


                    
            elif user.lower() == "b":
                self.sign_up()
        



                                                # Home page



    def home_page(self):
        time.sleep(2)
        val = (self.username, self.password)
        print("Home page".center(180))
        print(f"""
                                                                                Welcome back {self.username}
        """)
    
        print("""
                                                                    1. Buy airtime                    6. Help 
                                                                    2. Transfer                       7. History
                                                                    3. Check balance                  8. Me
                                                                    4. Deposit                        9. Log out
                                                                    5. Withdraw                       10. Exit
                                                        
                    
        """
        )
        
        user = input("\nEnter your choice: ")
        if user == "1":
            self.buy_airtime()
        elif user == "2":
            self.transfer()
        elif user == "3":
            self.check_balance()
        elif user == "4":
            self.deposit()
        elif user == "5":
            self.withdraw()   
        elif user == "6":
            self.help()
        elif user == "7":
            self.history()
        elif user == "8":
            self.me()
        elif user == "9":
            self.log_out()
        elif user == "10":
            self.exit()
        while user != "1" "2" "3" "4" "5" "6" "7" "8" "9" "10":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nEnter your choice: ')


            if user == "1":
                self.buy_airtime()
            elif user == "2":
                self.transfer()
            elif user == "3":
                self.check_balance()
            elif user == "4":
                self.deposit()
            elif user == "5":
                self.withdraw()   
            elif user == "6":
                self.help()
            elif user == "7":
                self.history()
            elif user == "8":
                self.me()
            elif user == "9":
                self.log_out()
            elif user == "10":
                self.exit()


                                                           
                                                           
                                                            # Buy Airtime

    def buy_airtime(self):
        time.sleep(1)
        print("""
                                                                                    Buy Airtime
        """)
        time.sleep(1)
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        self.balance = detail[0][0]
        print(f"""
                                                                        Your account balance is #{detail[0][0]}
        """)

        print("\n1. For self \n2. For others")
        user = input("\nEnter your choice: ")

        if user == "1":
            self.for_self()
        elif user == "2":
            self.for_others()


                                                
                                                
                                                # Buy Airtime for self



    def for_self(self):
        time.sleep(1.5)
        self.buy_airtime1 = float(input('\nPlease enter an amount: '))
        time.sleep(1)
        if self.buy_airtime1 >= self.balance:
                time.sleep(1)
                print("\nInsufficient fund.")
                time.sleep(0.5)
                print("\n1. Deposit \n2. Back")

                customer = input("\nPlease choose an option: ")

                if customer == "1":
                    self.deposit()
                elif customer == "2":
                    self.home_page()    

        elif self.buy_airtime1 <= self.balance:
            time.sleep(2)
            print(f"\nYou have successfully recharge #{self.buy_airtime1} airtime.")

            self.balance -= self.buy_airtime1


            query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
            val = (self.balance, self.username, self.password)
            mycursor.execute(query, val)        
            mycon.commit()
            time.sleep(2)
            print(f'\nYour new balance is #{self.balance}')
            time.sleep(0.5)

            query1 = "INSERT INTO transaction_table(transaction_type, amount, username, date_time) VALUES(%s,%s,%s,%s)"
            transaction_type = 'Airtime for self'
            amount = self.buy_airtime1
            date_time = dt.datetime.now()
            val1 = (transaction_type, amount, self.username, date_time)
            mycursor.execute(query1, val1)
            mycon.commit()

            print("\nPress A to go back or B to exit: ")
            user = input("\nEnter your choice: ")

            if user.lower() == "a":
                self.home_page()
            elif user.lower() == "b":
                sys.exit()
                time.sleep(0.5)





                                                  
                                                  
                                                    # Buy Airtime for others



    def for_others(self):
        time.sleep(1)
        print("""
                                                                                Buy Airtime for others
        """)
        time.sleep(1)
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        self.balance = detail[0][0]
        print(f"""
                                                                        Your account balance is #{detail[0][0]}
        """)
        self.buy_airtime2 = float(input('\nPlease enter an amount: '))
        time.sleep(1)
        if self.buy_airtime2 >= self.balance:
            time.sleep(1)
            print("\nInsufficient fund.")
            time.sleep(0.5)
            print("\n1. Deposit \n2. Back")

            customer = input("\nPlease choose an option: ")

            if customer == "1":
                self.deposit()
            elif customer == "2":
                self.home_page()
        elif self.buy_airtime2 <= self.balance:
            number = print("\nPlease enter the recipients phone number")

            self.user2 = input("\nRecipients number: ")
            self.number()

    def number(self):
        time.sleep(0.5)
        print("\nPlease choose a network\n \n1. MTN \n2. Airtel \n3. GLO")
        

        user = input("\nEnter your choice: ")
        if user == "1":
            time.sleep(1.5)
            if self.buy_airtime2:
                time.sleep(2)
                print(f"\nYou have successfully recharge #{self.buy_airtime2} airtime for {self.user2}.")

                self.balance -= self.buy_airtime2


                query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
                val = (self.balance, self.username, self.password)
                mycursor.execute(query, val)        
                mycon.commit()
                time.sleep(2)
                print(f'\nYour new balance is #{self.balance}')
                time.sleep(0.5)

                query1 = "INSERT INTO transaction_table(transaction_type, amount, beneficiary, username, date_time) VALUES(%s,%s,%s,%s,%s)"
                transaction_type = 'Airtime for others'
                amount = self.buy_airtime2
                beneficiary = self.user2
                date_time = dt.datetime.now()
                val1 = (transaction_type, amount, beneficiary, self.username, date_time)
                mycursor.execute(query1, val1)
                mycon.commit()

                print("\nPress A to go back or B to exit: ")
                user = input("\nEnter your choice: ")

                if user.lower() == "a":
                    self.home_page()
                elif user.lower() == "b":
                    sys.exit()
                    time.sleep(0.5)
        elif user == "2":
            if self.buy_airtime2:
                time.sleep(2)
                print(f"\nYou have successfully recharge #{self.buy_airtime2} airtime for {self.user2}.")

                self.balance -= self.buy_airtime2


                query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
                val = (self.balance, self.username, self.password)
                mycursor.execute(query, val)        
                mycon.commit()
                time.sleep(2)
                print(f'\nYour new balance is #{self.balance}')
                time.sleep(0.5)

                query1 = "INSERT INTO transaction_table(transaction_type, amount, beneficiary, username, date_time) VALUES(%s,%s,%s,%s,%s)"
                transaction_type = 'Airtime for others'
                amount = self.buy_airtime2
                beneficiary = self.user2
                date_time = dt.datetime.now()
                val1 = (transaction_type, amount, beneficiary, self.username, date_time)
                mycursor.execute(query1, val1)
                mycon.commit()

                print("\nPress A to go back or B to exit: ")
                user = input("\nEnter your choice: ")

                if user.lower() == "a":
                    self.home_page()
                elif user.lower() == "b":
                    sys.exit()
                    time.sleep(0.5)
        elif user == "3":
            if self.buy_airtime2:
                time.sleep(2)
                print(f"\nYou have successfully recharge #{self.buy_airtime2} airtime for {self.user2}.")

                self.balance -= self.buy_airtime2


                query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
                val = (self.balance, self.username, self.password)
                mycursor.execute(query, val)        
                mycon.commit()
                time.sleep(2)
                print(f'\nYour new balance is #{self.balance}')
                time.sleep(0.5)

                query1 = "INSERT INTO transaction_table(transaction_type, amount, beneficiary, username, date_time) VALUES(%s,%s,%s,%s,%s)"
                transaction_type = 'Airtime for others'
                amount = self.buy_airtime2
                beneficiary = self.user2
                date_time = dt.datetime.now()
                val1 = (transaction_type, amount, beneficiary, self.username, date_time)
                mycursor.execute(query1, val1)
                mycon.commit()

                print("\nPress A to go back or B to exit: ")
                user = input("\nEnter your choice: ")

                if user.lower() == "a":
                    self.home_page()
                elif user.lower() == "b":
                    sys.exit()
                    time.sleep(0.5)




                                                     # Transfer



    def transfer(self):
        time.sleep(1)
        print("""
                                                                                    Transfer page
        """)
        time.sleep(1)
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        self.balance = detail[0][0]
        print(f"""
                                                                        Your account balance is #{detail[0][0]}
        """)

        self.user = print("\nPlease enter the beneficiary account number")

        self.account_no = input("\nBeneficiary account number: ")
        time.sleep(1)
        query5 = ("SELECT account_no FROM customer_table WHERE username=%s and password=%s")
        val = (self.username, self.password)
        mycursor.execute(query5, val)
        detail = mycursor.fetchall()
        while detail:
            time.sleep(1)
            print("\nCannot transfer to the same account number")
            self.user = print("\nPlease enter the beneficiary account number")

            self.account_no = input("\nBeneficiary account number: ")
            time.sleep(1)
            if self.account_no:
                query = ("SELECT account_no FROM customer_table WHERE username=%s and password=%s")
                val1 = (self.username, self.password)
                mycursor.execute(query, val1)
                detail = mycursor.fetchall()
                query2 = ("SELECT fullname FROM customer_table WHERE account_no=%s")
                val2 = (self.account_no,)
                mycursor.execute(query2, val2)
                self.detail1 = mycursor.fetchall()
                self.output = self.detail1
                if self.output:
                    print(f"\nYou want to transfer to {self.account_no}")
                    query1 = ("SELECT account_no, account_bal, fullname FROM customer_table WHERE account_no=%s")
                    val1 = (self.account_no,)
                    mycursor.execute(query1, val1)
                    detail = mycursor.fetchall()
                    # print(detail)
                    self.balance_benef = detail[0][1]
                    self.transfer1 = float(input('\nPlease enter the amount you want to transfer: '))
                    time.sleep(1)
                    self.balance_benef += self.transfer1
                    if self.transfer1 >= self.balance:
                        time.sleep(1)
                        print("\nInsufficient fund.")
                        time.sleep(0.5)
                        print("\n1. Deposit \n2. Back")

                        customer1 = input("\nPlease choose an option: ")
                        if customer1 == "1":
                            self.deposit()
                        elif customer1 == "2":
                            self.home_page()
                        while customer1 != "1" "2":
                            time.sleep(1)
                            print('\nInvalid input!!')
                            customer1 = input('\nChoose an option: ')

                            if customer1 == "1":
                                self.deposit()
                            elif customer1 == "2":
                                self.home_page()    
                            # self.fullname1 = print({self.fullname})
                    elif self.transfer1 <= self.balance:
                        query = 'UPDATE customer_table SET account_bal = %s WHERE account_no=%s'
                        val = (self.balance_benef, self.account_no,)
                        mycursor.execute(query, val)
                        mycon.commit()
                        time.sleep(1)
                        
                        if detail:
                            self.beneficiary_accountnumber()
                else:
                    while self.account_no != "account_no":
                        time.sleep(1)
                        print('\nInvalid account number!!')
                        self.account_no = input('\nEnter correct account number: ')

                        if self.account_no:
                            # self.output
                            time.sleep(1)
                            query2 = ("SELECT fullname FROM customer_table WHERE account_no=%s")
                            val2 = (self.account_no,)
                            mycursor.execute(query2, val2)
                            self.detail1 = mycursor.fetchall()
                            self.output = self.detail1
                            print(f"\nYou want to transfer to {self.account_no}")
                            query1 = ("SELECT account_no, account_bal, fullname FROM customer_table WHERE account_no=%s")
                            val1 = (self.account_no,)
                            mycursor.execute(query1, val1)
                            detail = mycursor.fetchall()
                            # print(detail)
                            self.balance_benef = detail[0][1]
                            self.transfer1 = float(input('\nPlease enter the amount you want to transfer: '))
                            time.sleep(1)
                            self.balance_benef += self.transfer1
                            if self.transfer1 >= self.balance:
                                time.sleep(1)
                                print("\nInsufficient fund.")
                                time.sleep(0.5)
                                print("\n1. Deposit \n2. Back")

                                customer = input("\nPlease choose an option: ")
                                if customer == "1":
                                    self.deposit()
                                elif customer == "2":
                                    self.home_page() 
                                while customer != "1" "2":
                                    time.sleep(1)
                                    print('\nInvalid input!!')
                                    customer = input('\nChoose an option: ')

                                    if customer == "1":
                                        self.deposit()
                                    elif customer == "2":
                                        self.home_page()    
                                # self.fullname1 = print({self.fullname})

                            elif self.transfer1 <= self.balance:
                                query = 'UPDATE customer_table SET account_bal = %s WHERE account_no=%s'
                                val = (self.balance_benef, self.account_no,)
                                mycursor.execute(query, val)
                                mycon.commit()
                                time.sleep(1)
                                
                                if detail:
                                    self.beneficiary_accountnumber()

    def beneficiary_accountnumber(self):
        time.sleep(1)
        if self.account_no:
            print(f"\nYou have successfully transfer #{self.transfer1} to {self.account_no}.")
            



        self.balance -= self.transfer1

                        
                                            # User account update

        query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
        val = (self.balance, self.username, self.password)
        mycursor.execute(query, val)        
        mycon.commit()
        time.sleep(2)
        print(f'\nYour new balance is #{self.balance}')
        time.sleep(0.5)

        query1 = "INSERT INTO transaction_table(transaction_type, amount, beneficiary, username, date_time) VALUES(%s,%s,%s,%s,%s)"
        transaction_type = 'Transfer'
        amount = self.transfer1
        beneficiary = self.account_no
        date_time = dt.datetime.now()
        val1 = (transaction_type, amount, beneficiary, self.username, date_time)
        mycursor.execute(query1, val1)
        mycon.commit()

        print("\nDid you want to make another transaction?\n \n1. Yes \n2. No")
        user = input("\nEnter your choice: ")
        if user == "1":
            self.transfer()
        elif user == "2":
            time.sleep(1)
            print("\nPress A to go back or B to exit: ")
            user = input("\nEnter your choice: ")
            if user == "a":
                self.home_page()
            elif user == "b":
                sys.exit()
                time.sleep(0.5)
            while user != "a" "b":
                time.sleep(1)
                print('\nInvalid input!!')
                user = input('\nEnter your choice: ')

                if user == "A":
                    self.home_page()
                elif user == "B":
                    sys.exit()
                    time.sleep(0.5)
        while user != "1" "2":
            time.sleep(1)
            print('\nInvalid input!!')
            user = input('\nEnter your choice: ')

            if user == "1":
                self.transfer()
            elif user == "2":
                time.sleep(1)
                print("\nPress A to go back or B to exit: ")
                user = input("\nEnter your choice: ")
                while user != "a" "b":
                    time.sleep(1)
                    print('\nInvalid input!!')
                    user = input('\nEnter your choice: ')

                    if user == "a":
                        self.home_page()
                    elif user == "b":
                        sys.exit()
                        time.sleep(0.5)





                                                 # Check balance


    def check_balance(self):
        time.sleep(1)
        print("""
                                                                                    Check Balance
        """)
        time.sleep(3)
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        # print(detail)
        print(f"""
                                                                        Your account balance is #{detail[0][0]}
        """)
        time.sleep(1)
        print("\nPress A to deposit, B to go back to main or C to exit: ")
        user = input("\nEnter your choice: ")

        if user.lower() == "a":
            self.deposit()
        elif user.lower() == "b":
            self.home_page()
        elif user.lower() == "c":
            sys.exit()
            time.sleep(0.5)

        while user.lower() != "a" "b" "c":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nTry again\n \nEnter your choice:  ')


            if user.lower() == "a":
                self.deposit()
            elif user.lower() == "b":
                self.home_page()
            elif user.lower() == "c":
                sys.exit()
                time.sleep(0.5)



                                                    # Deposit



    def deposit(self):
        time.sleep(1)
        print("""
                                                                                        Deposit
        """)
        time.sleep(1)
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        balance = detail[0][0]
        # print(detail)
        print(f"""
                                                                        Your account balance is #{detail[0][0]}
        """)
        deposit = float(input('\nPlease enter the amount you want to deposit: '))
        balance += deposit

        # updating the customer account balance
        query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
        val = (balance, self.username, self.password)
        mycursor.execute(query, val)        
        mycon.commit()
        print("\nLoading...")
        time.sleep(2)
        print(f'\nYour new balance is #{balance}')
        time.sleep(0.5)

        query1 = "INSERT INTO transaction_table(transaction_type, amount, username, date_time) VALUES(%s,%s,%s,%s)"
        transaction_type = 'Deposit'
        amount = deposit
        date_time = dt.datetime.now()
        val1 = (transaction_type, amount, self.username, date_time)
        mycursor.execute(query1, val1)
        mycon.commit()

        print("\nPress A to go back or B to exit: ")
        user = input("\nEnter your choice: ")
        if user== "a":
            self.home_page()
        elif user== "b":
            sys.exit()
            time.sleep(0.5)
        while user != "a" "b":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nEnter your choice: ')

            if user== "a":
                self.home_page()
            elif user== "b":
                sys.exit()
                time.sleep(0.5)
    



                                                    
                                                    # Withdraw
                                                    


    def withdraw(self):
        time.sleep(1)
        print("""
                                                                                        Withdraw
        """)
        time.sleep(1)
        query = "SELECT account_bal FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        balance = detail[0][0]
        print(f"""
                                                                       Your account balance is #{detail[0][0]} 
        """)
        self.withdraw = float(input('\nPlease enter the amount you want to withdraw: '))
        if self.withdraw >= balance:
            time.sleep(1)
            print("\nInsufficient fund.")
            time.sleep(0.5)
            print("\n1. Deposit \n2. Back")

            customer = input("\nPlease choose an option: ")
            if customer == "1":
                self.deposit()
            elif customer == "2":
                self.home_page()
            while customer != "1" "2":
                time.sleep(1)
                customer = input('\nInvalid input!!\n \nEnter your choice: ')

                if customer== "1":
                    self.home_page()
                elif customer== "2":
                    sys.exit()
                    time.sleep(0.5)

                if customer == "1":
                    self.deposit()
                elif customer == "2":
                    self.home_page()
        elif self.withdraw <= balance:
            balance -= self.withdraw

            query = 'UPDATE customer_table SET account_bal = %s WHERE username = %s AND password = %s'
            val = (balance, self.username, self.password)
            mycursor.execute(query, val)        
            mycon.commit()
            print("\nLoading...")
            time.sleep(2)
            print(f"\nYou have successfully withdraw #{self.withdraw}")
            time.sleep(0.5)
            print(f'\nYour new balance is #{balance}')
            time.sleep(1)

            
            query1 = "INSERT INTO transaction_table(transaction_type, amount, username, date_time) VALUES(%s,%s,%s,%s)"
            transaction_type = 'Withdraw'
            amount = self.withdraw
            date_time = dt.datetime.now()
            val1 = (transaction_type, amount, self.username, date_time)
            mycursor.execute(query1, val1)
            mycon.commit()


            print("\nDid you want to make another transaction?\n \n1. Yes \n2. No")
            user = input("\nEnter your choice: ")
            if user == "1":
                self.withdraw()
            elif user == "2":
                time.sleep(1)
                print("\nPress A to go back or B to exit: ")
                user = input("\nEnter your choice: ")

                if user.lower() == "a":
                    self.home_page()
                elif user.lower() == "b":
                    sys.exit()
                    time.sleep(0.5)
                while user != "a" "b":
                    time.sleep(1)
                    user = input('\nInvalid input!!\n \nEnter your choice: ')

                    if user.lower() == "a":
                        self.home_page()
                    elif user.lower() == "b":
                        sys.exit()
                        time.sleep(0.5)

            while user != "1" "2":
                time.sleep(1)
                user = input('\nInvalid input!!\n \nEnter your choice: ')
                if user == "1":
                    self.withdraw()
                elif user == "2":
                    time.sleep(1)
                    print("\nPress A to go back or B to exit: ")
                    user = input("\nEnter your choice: ")

                    if user.lower() == "a":
                        self.home_page()
                    elif user.lower() == "b":
                        sys.exit()
                        time.sleep(0.5)
                    while user != "a" "b":
                        time.sleep(1)
                        user = input('\nInvalid input!!\n \nEnter your choice: ')

                        if user.lower() == "a":
                            self.home_page()
                        elif user.lower() == "b":
                            sys.exit()
                            time.sleep(0.5)


                                                            # Help

    
    def help(self):
        time.sleep(1)
        print("""
                                                                                         Help
        """)
        time.sleep(1)
        print("""
                                                                                    1. Contact us
                                                                                    2. Email us
                                                                                    3. Chat with us
        """)
        user = input("\nEnter your choice: ")
        if user == "1":
            self.contact_us()
        elif user == "2":
            self.email_us()
        elif user == "3":
            self.chat_with_us()
        while user != "1" "2" "3":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nEnter your choice: ')
            if user == "1":
                self.contact_us()
            elif user == "2":
                self.email_us()
            elif user == "3":
                self.chat_with_us()

    def contact_us(self):
        time.sleep(1)
        print("""
                                                                                        Contact us
        """)
        time.sleep(1)
        print("""
                                                                                Hi, let's help you today.

                                                                Phone lines are available between 8:00 AM and 5:00 PM on weekdays.

                                                                                    Call the number below

                                                                                        +2349045348114  
        """)
        time.sleep(1)
        print("\nPress A to go back, B to go back to home page or C to exit: ")
        user = input("\nEnter your choice: ")

        if user.lower() == "a":
            self.help()
        elif user.lower() == "b":
            self.home_page()
        elif user.lower() == "c":
            sys.exit()
            time.sleep(0.5)
        while user != "a" "b" "c":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nEnter your choice: ')
            if user.lower() == "a":
                self.help()
            elif user.lower() == "b":
                self.home_page()
            elif user.lower() == "c":
                sys.exit()
                time.sleep(0.5)

    def email_us(self):
        time.sleep(1)
        print("""
                                                                                        Email us
        """)
        time.sleep(1)
        print("""
                                                                    You can email us on: elijahayanlere3@gmail.com
        """)
        time.sleep(1)
        print("\nPress A to go back, B to go back to home page or C to exit: ")
        user = input("\nEnter your choice: ")

        if user.lower() == "a":
            self.help()
        elif user.lower() == "b":
            self.home_page()
        elif user.lower() == "c":
            sys.exit()
            time.sleep(0.5)
        while user != "a" "b" "c":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nEnter your choice: ')
            if user.lower() == "a":
                self.help()
            elif user.lower() == "b":
                self.home_page()
            elif user.lower() == "c":
                sys.exit()
                time.sleep(0.5)

    def chat_with_us(self):
        time.sleep(1)
        print("""
                                                                                    Chat with us
        """)
        time.sleep(1)
        time.sleep(1)
        import bank_app_chatbot

                                                        
                                                        # History


    def history(self):
        time.sleep(1)
        print("""
                                                                                    History page
        """)

        query3 = "SELECT transaction_id, transaction_type, amount, beneficiary, date_time FROM transaction_table WHERE username = %s"
        val3 = (self.username,)
        mycursor.execute(query3, val3)
        detail = mycursor.fetchall()
        detail1 = detail
        print(detail1)
        time.sleep(1)
        print("\nPress A to go back or B to exit: ")
        user = input("\nEnter your choice: ")

        if user.lower() == "a":
            self.home_page()
        elif user.lower() == "b":
            sys.exit()
            time.sleep(0.5)
        while user != "a" "b":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nEnter your choice: ')
            if user.lower() == "a":
                self.home_page()
            elif user.lower() == "b":
                sys.exit()
                time.sleep(0.5)




                                                    
                                                    # Me


    def me(self):
        time.sleep(1)
        print(f"""
                                                                                    Welcome {self.username}
        """)
        time.sleep(3)
        query = "SELECT account_bal, bvn, account_no FROM customer_table WHERE username = %s and password = %s"
        val = (self.username, self.password)
        mycursor.execute(query, val)
        detail = mycursor.fetchall()
        print(f"""
                                                                        Your account balance is #{detail[0][0]}
        """)
        query1 = "SELECT email FROM customer_table WHERE username = %s and password = %s"
        Val1 = (self.username, self.password)
        mycursor.execute(query1, Val1)
        detail1 = mycursor.fetchall()
        print(f"""
                                                                Your email address is {detail1}
        """)
        query2 = "SELECT phone_number FROM customer_table WHERE username = %s and password = %s"
        Val2 = (self.username, self.password)
        mycursor.execute(query2, Val2)
        detail2 = mycursor.fetchall()
        print(f"""
                                                                        Your phone number is {detail2}
        """)
        query3 = "SELECT bvn FROM customer_table WHERE username = %s and password = %s"
        Val3 = (self.username, self.password)
        mycursor.execute(query3, Val3)
        detail3 = mycursor.fetchall()
        print(f"""
                                                                        Your bvn number is {detail3}
        """)
        query4 = "SELECT account_no FROM customer_table WHERE username = %s and password = %s"
        Val4 = (self.username, self.password)
        mycursor.execute(query4, Val4)
        detail4 = mycursor.fetchall()
        print(f"""
                                                                       Your account number is {detail4}
        """)
        # print(detail)
        time.sleep(1)
        print("\nPress A to go back or B to exit: ")
        user = input("\nEnter your choice: ")

        if user.lower() == "a":
            self.home_page()
        elif user.lower() == "b":
            sys.exit()
            time.sleep(0.5)
        while user != "a" "b":
            time.sleep(1)
            user = input('\nInvalid input!!\n \nEnter your choice: ')
            if user.lower() == "a":
                self.home_page()
            elif user.lower() == "b":
                sys.exit()
                time.sleep(0.5)
        

                                                    

                                                    
                                                    # Log out


    
    def log_out(self):
        query = "SELECT username, password FROM customer_table WHERE username = %s AND password = %s"
        time.sleep(1)
        print('''
                                                                                    Log out page
        ''')
        val = (self.username, self.password)
        mycursor.execute(query, val)
        output = mycursor.fetchall()
        time.sleep(1)
        print("\nPress A to log out or B to go back")
        user = input("\nEnter your choice: ")
        time.sleep(1)
        if user.lower() == "a":
            time.sleep(1)
            print("\nAre you sure you want to log out?\n \n1. Yes \n2. No")
            self.user5 = input("\nEnter your choice: ")
            if self.user5 == "1":
                print('\nPlease wait...')
                time.sleep(1.5)
                print("\nLog out successfully")
                time.sleep(0.5)
                self.log_in()
            elif self.user5 == "2":
                self.home_page()
            while self.user5 != "1" "2":
                time.sleep(1)
                print('\nInvalid input!! Try again!!')
                print("\nAre you sure you want to log out?\n \n1. Yes \n2. No")
                self.user6 = input('\nEnter your choice: ')
                if self.user6 == "1":
                    print('\nPlease wait...')
                    time.sleep(1.5)
                    print("\nLog out successfully")
                    time.sleep(0.5)
                    self.log_in()
                elif self.user6 == "2":
                    self.home_page()
        elif user.lower() == "b":
            self.home_page()
        while user != "a" "b":
            time.sleep(1)
            user1 = input('\nInvalid input!!\n \nEnter your choice: ')
            if user1.lower() == "a":
                time.sleep(1)
                print("\nAre you sure you want to log out?\n \n1. Yes \n2. No")
                self.user2 = input("\nEnter your choice: ")
                if self.user2 == "1":
                    print('\nPlease wait...')
                    time.sleep(1.5)
                    print("\nLog out successfully")
                    time.sleep(0.5)
                    self.log_in()
                elif self.user2 == "2":
                    self.home_page()
                while self.user2 != "1" "2":
                    time.sleep(1)
                    print('\nInvalid input!! Try again!!')
                    print("\nAre you sure you want to log out?\n \n1. Yes \n2. No")
                    self.user3 = input('\nEnter your choice: ')
                    if self.user3 == "1":
                        print('\nPlease wait...')
                        time.sleep(1.5)
                        print("\nLog out successfully")
                        time.sleep(0.5)
                        self.log_in()
                    elif self.user3 == "2":
                        self.home_page()
            elif user1.lower() == "b":
                self.home_page()


            

        
                                                        
                                                        # HELP


    def help1(self):
        time.sleep(1)
        print("""
                                                                                         Help
        """)
        time.sleep(1)
        print("""
                                                                                    1. Contact us
                                                                                    2. Email us
                                                                                    3. Chat with us
        """)
        user = input("\nEnter your choice: ")
        if user == "1":
            self.contact_us1()
        elif user == "2":
            self.email_us1()
        elif user == "3":
            self.chat_with_us1()

    def contact_us1(self):
        time.sleep(1)
        print("""
                                                                                        Contact us
        """)
        time.sleep(1)
        print("""
                                                                                Hi, let's help you today.

                                                                Phone lines are available between 8:00 AM and 5:00 PM on weekdays.

                                                                                Call the number below

                                                                                    +2349045348114  
        """)
        time.sleep(1)
        print("\nPress A to log in, B to sign up or C to exit: ")
        user = input("\nEnter your choice: ")

        if user.lower() == "a":
            self.log_in()
        elif user.lower() == "b":
            self.sign_up()
        elif user.lower() == "c":
            sys.exit()
            time.sleep(0.5)

    def email_us1(self):
        time.sleep(1)
        print("""
                                                                                        Email us
        """)
        time.sleep(1)
        print("""
                                                                    You can email us on: elijahayanlere3@gmail.com
        """)
        time.sleep(1)
        print("\nPress A to log in, B to sign up or C to exit: ")
        user = input("\nEnter your choice: ")

        if user.lower() == "a":
            self.log_in()
        elif user.lower() == "b":
            self.sign_up()
        elif user.lower() == "c":
            sys.exit()
            time.sleep(0.5)

    def chat_with_us1(self):
        time.sleep(1)
        print("""
                                                                                    Chat with us
        """)
        time.sleep(1)
        time.sleep(1)
        import bank_app_chatbot



                                                            # Exit

    def exit(self):
        sys.exit()
        time.sleep(0.5)
            



ussd = Page('Elijah')