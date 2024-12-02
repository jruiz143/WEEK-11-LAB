#PROGRAMMING EXERCISE 11-3
# WRITE A CLASS NAMED PERSON WITH DATA ATTRIBUTES FOR:
#A PERSON'S NAME, ADDRESS, AND TELEPHONE NUMBER.

#NEXT, WRITE A CLASS NAMED CUSTOMER THAT IS A SUBCLASS OF THE PERSON CLASS.
#THE CUSTOMER SHOULD HAVE A DATA ATTRIBUTE FOR A CUSTOMER NUMBER, AND A BOOLEAN DATA
#ATTRIBUTE INDICATING WHETHER THE CUSTOMER WISHES TO BE ON A MAILING LIST.
#DEMONSTRATE AN INSTANCE OF THE CUSTOMER CLASS IN A SIMPLE PROGRAM
#

#CREATE PERSON CLASS
class Person:
      #INITIALIZE THE OBJECT: 
      def __init__(self, name, address, phone):
            self.__name = name
            self.__address = address
            self.__phone = phone
      #SET MUTATORS FOR ATTRIUBUTES
      def set_name(self, name):
            self.__name = name
      def set_address(self, address):
            self.__address = address
      def set_phone (self, phone):
            self.__phone = phone
      #SET ACCESSORS FOR ATTRIBUTES
      def get_name (self):
            return self.__name
      def get_address(self):
            return self.__address
      def get_phone (self): 
            return self.__phone
      
#CREATE CUSTOMER CLASS
class Customer(Person): #THE CUSTOMER CLASS INHERITS WHAT'S IN THE PERSON CLASS(which is inside parantheses)
      #INITIALIZE THE CUSTOMER OBJECT WITH THE ADDITIONAL ATTRIBUTES(CUSTOMER NUMBER AND MAILING LIST):
      def __init__(self, name, address, phone, 
                   customer_number, mailing_list):
            #CALL THE INITIALIZER OF PERSON CLASS TO SET INHERITED ATTRIBUTES
            super().__init__(name, address, phone)
            #INITIALIZE THE SPECIALIZED ATTRIBUTES
            self.__customer_number = customer_number
            self.__mailing_list = mailing_list
      #SET MUTATORS FOR ATTRIBUTES
      def set_customer_number(self, customer_number):
            self.__customer_number = customer_number
      def set_mailing_list(self, mailing_list):
            self.__mailing_list = mailing_list
      #GET ACCESSORS FOR ATTRITUBUTES
      def get_customer_number(self):
            return self.__customer_number
      def get_mailing_list(self):
            return self.__mailing_list

# CREATE FUNCTION FOR CUSTOMER INFORMATION
def main():
    print("CUSTOMER INFORMATION")
    name = input("NAME: ")
    address = input("ADDRESS: ")
    phone = input("PHONE: ")
    customer_number = input("CUSTOMER NUMBER: ")
    mail = input("INCLUDE IN MAILING LIST? (Y/N): ")

    # CHECK IF CUSTOMER WANTS TO BE INCLUDED IN MAILING LIST
    if mail.lower() == 'y':
        mailing_list = True
    else:
        mailing_list = False
    #CREATE CUSTOMER OBJECT
    my_customer = Customer(name, address, phone, customer_number, mailing_list)

    #DISPLAY CUSTOMER INFO
    print("\nCUSTOMER INFOMATION")
    print("Name: ", my_customer.get_name())
    print("Address: ", my_customer.get_address())
    print("Phone: ", my_customer.get_phone())
    print("Customer Number: ", my_customer.get_customer_number())
    print("Included in Mailing List: ", my_customer.get_mailing_list())


# RUN THE MAIN FUNCTION
if __name__ == "__main__":
    main()
      


