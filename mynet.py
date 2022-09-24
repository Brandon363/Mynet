import streamlit as st

from streamlit_option_menu import option_menu

selected_menu = option_menu(
        menu_title = None,
        options = ["Home", "About The Developer", "Contact"],
        icons = ["house", "person-workspace","envelope"],
        menu_icon = "cast",
        orientation = "horizontal"
)


nav = st.sidebar.radio("Navigation",["Register", "Login", "Check Balance", "Make payment", "Send money", "Cash-in", "Cash-out", "Show database","Show Registered"])

    

class Mynet_Customer():
    #all_entries = []
    reserve     = 100
    import pandas as pd

    def __init__(self):
        import pandas as pd
        self.data     = pd.read_csv("Mynet_db.csv")
        self.data_new = pd.read_csv("Mynet_Reg.csv")
        
    ##############################    Register    ################################

    def Register(self):
        import pandas as pd
        self.id       = id_
        self.name     = name
        self.password = password
        self.number   = number 
        self.balance  = balance 

        to_add = {"id":[self.id],"name":[self.name],"password":[self.password],"number":[self.number],"balance":[self.balance]}
        to_add = pd.DataFrame(to_add)
        to_add.to_csv("Mynet_Reg.csv",  mode='a',header = False, index= False)
        to_add.to_csv("Mynet_db.csv",mode='a',header = False, index= False)
        
        self.data     = pd.read_csv("Mynet_db.csv")
        self.data_new = pd.read_csv("Mynet_Reg.csv")     

        st.success("You have successfully registered")

    

    #################################     Login    # ###############################

    def Login(self):
        self.entered_name     = name
        self.entered_password = password
        if len(self.data.loc[self.data["password"] == self.entered_password]) == 1 and \
           len(self.data.loc[self.data["name"] == self.entered_name]) == 1:
            self.login_status      = True
            self.Details      = self.data.loc[self.data["password"] == self.entered_password]
            self.C_id         = self.Details.iloc[0,0] #Ger the customer id
            self.C_name       = self.Details.iloc[0,1] #Ger the customer name
            self.C_password   = self.Details.iloc[0,2] #Ger the customer password
            self.C_number       = self.Details.iloc[0,3] #Ger the customer number 
            self.C_balance    = self.Details.iloc[0,4] #Ger the customer balance
            st.success(f"Welcome {self.C_name}")
        else:
            self.login_status      = False
            st.error("Password error: Login failed")

    #################################    check_balance    # ###############################

    def check_balance(self):
        self.Login()
        if self.login_status == False: #failed to login
            pass        
        else:
            st.success(f"\n\nYour acc balance is ${self.C_balance}")


    #################################    make_payment    # ###############################

    def make_payment(self):
        self.Login()
        if self.login_status == False: #failed to login
            pass        
        else:
            self.pay_amount = pay_amount
            if type(self.pay_amount) == float:
                if self.C_balance >= self.pay_amount:
                    self.new_C_balance = self.C_balance - self.pay_amount
                    st.success(f"""You have successfully made a payment of ${self.pay_amount} 
                           \nYour new balance is ${self.new_C_balance}""")

                    self.data.loc[self.data["id"]==self.C_id, "balance"] = self.new_C_balance 
                    
                    import pandas as pd
                    to_add2 = self.data
                    to_add2.to_csv("Mynet_db.csv",header = True, index= False)
        
                    self.data     = pd.read_csv("Mynet_db.csv")
                    #self.data_new = pd.read_csv("Mynet_Reg.csv")      

                else:
                    st.error("You have insufficient funds to make this payment")
            else:
                st.error("invalid entry")


    ################################ Send_money ################################

    def send_money(self):
        self.Login()
        if self.login_status == False: #failed to login
            pass        
        else:
            self.receiver_num = receiver_num
            if len(self.data.loc[self.data["number"] == self.receiver_num]) == 1:
                
                
                self.receiver_Details   = self.data.loc[self.data["number"] == self.receiver_num]
                self.receiver_id        = self.receiver_Details.iloc[0,0] #Ger the customer id
                self.receiver_name      = self.receiver_Details.iloc[0,1] #Ger the customer name
                self.receiver_password  = self.receiver_Details.iloc[0,2] #Ger the customer password 
                self.receiver_balance   = self.receiver_Details.iloc[0,4] #Ger the customer balance
                
                if self.C_number == self.receiver_num:
                    st.error("\nYou cant send money to your own mobile number directly")
                
                else:
        
                    self.send_amount    = send_amount
                    self.confirm_status = confirm_status
                    if self.confirm_status == "1":
                        if self.C_balance >= self.send_amount:
                            self.new_balance_S = self.C_balance - self.send_amount
                            self.new_balance_R = self.receiver_balance + self.send_amount
                            
                            
                            self.data.loc[self.data["id"]==self.C_id, "balance"]        = self.new_balance_S
                            self.data.loc[self.data["id"]==self.receiver_id, "balance"] = self.new_balance_R
                            st.success(f"""You have successfully sent RTGS{self.send_amount} to {self.receiver_name}, You had RTGS{self.C_balance} Your new account balance is RTGS{self.new_balance_S}""")


                            import pandas as pd
                            to_add2 = self.data
                            to_add2.to_csv("Mynet_db.csv",header = True, index= False)
                
                            self.data     = pd.read_csv("Mynet_db.csv")



                        else:
                            st.error("\n\nYou have insufficient funds to complete this payment")
                    elif self.confirm_status == "2":
                        st.error("You have cancelled")
                    else:
                        st.error("invalid entry")
   
            else:
                st.error("Number is not registered")


    ################################ cashin ################################

    def cashin(self):
        
        self.Login()
        if self.login_status == False: #failed to login
            pass        
        else:
            self.cashin_amount =  cashin_amount
            if type(self.cashin_amount) == float:
                Mynet_Customer.reserve = Mynet_Customer.reserve - self.cashin_amount
                self.new_C_balance = self.C_balance + self.cashin_amount
                st.success(f"""\n\nYou have successfully cashed in RTGS{self.cashin_amount} 
                       \nYour new balance is RTGS{self.new_C_balance}""")

                self.data.loc[self.data["id"]==self.C_id, "balance"] = self.new_C_balance  

                import pandas as pd
                to_add2 = self.data
                to_add2.to_csv("Mynet_db.csv",header = True, index= False)
    
                self.data     = pd.read_csv("Mynet_db.csv")

            else:
                st.error("invalid entry")
                
   
    ################################ cashout ################################

    def cashout(self):
        
        self.Login()
        if self.login_status == False: #failed to login
            pass        
        else:
            self.cashout_amount = cashout_amount
            if type(self.cashout_amount) == float:
                if self.C_balance >= self.cashout_amount:
                    Mynet_Customer.reserve = Mynet_Customer.reserve + self.cashout_amount
                    self.new_C_balance = self.C_balance - self.cashout_amount
                    st.success(f"""\n\nYou have successfully cashed out ${self.cashout_amount} 
                           \nYour new balance is ${self.new_C_balance}""")

                    self.data.loc[self.data["id"]==self.C_id, "balance"] = self.new_C_balance

                    import pandas as pd
                    to_add2 = self.data
                    to_add2.to_csv("Mynet_db.csv",header = True, index= False)
        
                    self.data     = pd.read_csv("Mynet_db.csv")  

                else:
                    st.error("\n\nYou have insufficient funds to make this payment")
            else:
                print("invalid entry")




    ################################ Show Registered ################################
    
    def show_Registered(self):
        return st.dataframe(self.data_new)

    ############################### Show database ################################
 
    def show_database(self):
        return st.dataframe(self.data)

#------------------------------------Page 1 ----------------------------------------

if selected_menu == "Home":
   
    st.title("Mynet")

     ##############################    Register    ################################
    if nav == "Register":


        with st.form(key = "register"):
            id_      = st.text_input("Enter id       ")
            name     = st.text_input("Enter name      ")
            password = st.text_input("Enter password  ")
            number   = st.text_input("Enter phone number")
            balance  = 0
            
            reg_submit_button = st.form_submit_button(label="Register")

        if reg_submit_button:
            Mynet_Customer().Register()

    #################################     Login    # ###############################

    if nav == "Login":
        with st.form(key = "login"):
            name     = st.text_input(str("Enter name      "))
            password = st.text_input(str("Enter password  "))
    
            login_submit_button = st.form_submit_button(label="Login")

        if login_submit_button:
            Mynet_Customer().Login()

     #################################     check_balance    # ###############################

    if nav == "Check Balance":
        with st.form(key = "login"):
            name     = st.text_input(str("Enter name      "))
            password = st.text_input(str("Enter password  "))
    
            check_balance_submit_button = st.form_submit_button(label="Check Balance")

        if check_balance_submit_button:
            Mynet_Customer().check_balance()


    ################################ make_payment ###############################
    if nav == "Make payment":
        with st.form(key = "make payment"):
            name       = st.text_input(str("Enter name      "))
            password   = st.text_input(str("Enter password  "))
            pay_amount = float(st.number_input("Enter amount to be paid "))
    
            make_payment_submit_button = st.form_submit_button(label="Make payment")

        if make_payment_submit_button:
            Mynet_Customer().make_payment()


    
    ############################### Send money ################################
    
    if nav == "Send money":
        with st.form(key = "make payment"):
            name       = st.text_input(str("Enter name      "))
            password   = st.text_input(str("Enter password  "))
            receiver_num = st.number_input("Enter the mobile number to receive  ")
            send_amount  = st.number_input("\nEnter the amount to be sent  ")
            confirm_status = st.text_input( "1: confirm         \n2: cancel")
            # confirm_status = st.text_input(f"""\nSending ${send_amount} to {receiver_num}  
            #         \n1: confirm \n2: cancel  \n""")
    
            send_money_submit_button = st.form_submit_button(label="Send money")

        if send_money_submit_button:
            Mynet_Customer().send_money()

   
    ############################### cashin ################################
    
    if nav == "Cash-in":
        with st.form(key = "cashin"):
            name       = st.text_input(str("Enter name      "))
            password   = st.text_input(str("Enter password  "))
            cashin_amount    = float(st.number_input("Enter amount to cash in ")) 
    
            cashin_submit_button = st.form_submit_button(label="cashin")

        if cashin_submit_button:
            Mynet_Customer().cashin()


    ############################### cashout ################################
    
    if nav == "Cash-out":
        with st.form(key = "cashin"):
            name       = st.text_input(str("Enter name      "))
            password   = st.text_input(str("Enter password  "))
            cashout_amount    = float(st.number_input("Enter amount to cash out ")) 
    
            cashout_submit_button = st.form_submit_button(label="cashout")

        if cashout_submit_button:
            Mynet_Customer().cashout()

    


    


     ############################### Show database ################################

    if nav == "Show database":
        Mynet_Customer().show_database()

     ################################ Show Registered ################################

    if nav == "Show Registered":
        Mynet_Customer().show_Registered()


elif selected_menu == "About The Developer":
    #st.title("Who is he?")
    #st.write("The best there is")
    col1, col2 = st.columns(2)


    with col1:
        st.header("Brandon Mutombwa")
        st.image("my_pic/brandon_pic.jpg", caption = "Tonderai Brandon Mutombwa")
        
    with col2:
        st.write(" ")

    st.write("Brandon is a creative, Data Science student at the University of Zimbabwe who is enthusiastic about executing data driven solutions to increase efficiency, accuracy and utility of internal data processing. He is driven by a strong PASSION AND PURPOSE for solving data problems.")
   

 
   

elif selected_menu == "Contact":
    st.write("Calls     : +263 776 464 136/ +263 77 586 0625         \nWhatsApp : +263 776 464 136        \nEmail : brandonmutombwa@gmail.com")
