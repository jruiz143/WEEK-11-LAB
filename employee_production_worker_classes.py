#PROGRAMMING EXERCISE 11-1
# WRITE AN EMPLOYEE CLASS THAT KEEPS DATA ATTRIBUTES FOR THE
#FOLLOWING INFO: EMPLOYEE NAME AND EMPLOYEE NUMBER

#NEXT, WRITE A CLASS NAME ProductionWorker THAT IS A SUBCLASS OF THE EMPLOYEE CLASS.
#THE PRODUCTIONWORKER CLASS SHOULD KEEP DATA ATTRIBUTES FOR THE FOLLOWING INFO:
#SHIFT NUMBER (AN INTEGER, SUCH AS 1,2,3) AND HOURLY PAY RATE
#THE WORKDAY IS DIVIDED INTO TWO SHIFTS: DAY AND NIGHT.
#THE SHIFT ATTRIBUTE WILL HOLD AN INTEGER VALUE REPRESENTING THE SHIFT THE EMPLOYEE WORKS.
#THE DAT SHIFT IS SHIFT 1 AND THE NIGHT SHIFT IS SHIFT 2.
#WRITE THE APPROPIATE ACCESSOR AND MUTATOR METHODS FOR EACH CLASS.

#ONCE YOU HAVE WRITTEN THE CLASSES, WRITE A PROGRAM THAT CREATES AN OBJECT OF THE PRODUCTIONWORKER
#CLASS AND PROMPTS THE USER TO ENTER DATA FOR EACH OF THE OBJECTS DATA ATTRIBUTES.
#STORE THE DATA IN THE OBJECT, THEN USE THE OBJECTS ACCESSOR METHODS TO RETREIVE IT AND DISPLAY

# CREATE EMPLOYEE CLASS
class Employee:
    # INITIALIZE THE OBJECTS
    def __init__(self, employee_name, employee_number):
        self.__employee_name = employee_name
        self.__employee_number = employee_number

    # SET MUTATORS
    def set_employee_name(self, employee_name):
        self.__employee_name = employee_name

    def set_employee_number(self, employee_number):
        self.__employee_number = employee_number

    # SET ACCESSORS FOR ATTRIBUTES
    def get_employee_name(self):
        return self.__employee_name

    def get_employee_number(self):
        return self.__employee_number
          
#CREATE PRODUCTIONWORKER CLASS, (WHICH INHERITS FROM EMPLOYEE CLASS)
class ProductionWorker(Employee):
    # INITIALIZE ProductionWorker OBJECT W/ THE ADDITIONAL ATTRIBUTES 
    def __init__(self, name, employee_number, 
                 shift_number, hourly_pay_rate):
        # CALL THE INITALIZER OF THE EMPLOYEE CLASS
        super().__init__(name, employee_number)
        #INITIALIZE PRODUCTIONWORKER CLASS ATTRIBUTES
        self.__shift_number = shift_number 
        self.__hourly_pay_rate = hourly_pay_rate  

    # MUTATOR METHODS(SETTER)
    def set_shift_number(self, shift_number):
        self.__shift_number = shift_number

    def set_hourly_pay_rate(self, hourly_pay_rate):
        self.__hourly_pay_rate = hourly_pay_rate

    # ACCESSOR METHODS (GETTER)
    def get_shift_number(self):
        return self.__shift_number

    def get_hourly_pay_rate(self):
        return self.__hourly_pay_rate


# CREATE FUNCTION FOR NFORMATION INPUT
def main():
    # RETRIEVE USER INPUT
    print("PLEASE ENTER EMPLOYEE INFO:")
    name = input("Employee Name: ")
    employee_number = input("Employee Number: ")
    shift_number = int(input("Shift Number (1 = Day, 2 = Night): "))
    hourly_pay_rate = float(input("Hourly Pay Rate:$ "))


    # CREATE ProductionWorker OBJECT
    worker = ProductionWorker(name, employee_number, shift_number, hourly_pay_rate)

    # DISPLAY EMPLOYEE INFO
    print("\nEMPLOYEE INFORMATION:")
    print("NAME: ", worker.get_employee_name())
    print("EMPLOYEE NUMBER:", worker.get_employee_number())
    print("SHIFT:", worker.get_shift_number())
    print("HOURLY PAY RATE: $", worker.get_hourly_pay_rate())


# RUN MAIN
if __name__ == "__main__":
    main()