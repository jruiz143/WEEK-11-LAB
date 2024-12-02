#PROGRAMMING EXERCISE 11-2
#IN A PARTICULAR FACTORY, A SHIFT SUPERVISOR IS A SALARIED EMPLOYEE WHO SUPERVISES A SHIFT
#IN ADDITION TO A SALARY, THE SHIFT SUPERVISOR EARNS A YEARLY BONUS WHEN HIS OR HER SHIFTS MEETS PRODUCTION GOLS.
#WRITE A SHIFTSUPERVISOR CLASS THAT IS A SUBCLASS OF THE EMPLOYEE CLASS(EMPLOYEE_NAME, EMPLOYEE_NUMBER). 
#THE SHIFTSUPERVISOR CLASS SHOULD KEEP A DATA ATTRIBUTE FOR THE ANNUAL SALARY, AND A DATA ATTRIBUTE FOR THE ANNUAL
#PRODUCTION BONUS THAT A SHIFT SUPERVISOR HAS EARNED. DEMONSTRATE THE CLASS BY WRITING A PROGRAM THAT USES
#A SHIFTSUPERVISOR OBJECT.
#

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
class ShiftSupervisor(Employee):
    # INITIALIZE ShiftSupervisor OBJECT W/ THE ADDITIONAL ATTRIBUTES 
    def __init__(self, employee_name, employee_number, 
                 annual_salary, annual_production_bonus):
        #CALL THE INTIIALIZER OF THE EMPLOYEE CLASS
        super().__init__(employee_name, employee_number)
        #INITIALIZE shiftSupervisor CLASS ATTRIBUTES
        self.__annual_salary = annual_salary
        self.__annual_production_bonus = annual_production_bonus

    # MUTATOR METHODS(SETTER)
    def set_annual_salary(self, annual_salary):
        self.__annual_salary = annual_salary

    def set_annual_production_bonus(self, annual_production_bonus):
        self.__annual_production_bonus = annual_production_bonus

    # ACCESSOR METHODS (GETTER)
    def get_annual_salary(self):
        return self.__annual_salary

    def get_annual_production_bonus(self):
        return self.__annual_production_bonus
    # METHOD TO CALCULATE TOTAL COMPENSATION (SALARY + BONUS)
    def total_compensation(self):
        return self.__annual_salary + self.__annual_production_bonus

# CREATE FUNCTION TO DEMONSTRATE THE USE OF THE SHIFTSUPERVISOR CLASS
def main():
    # RETRIEVE USER INPUT
    print("INPUT SHIFT SUPERVISOR INFO:")
    name = input("Employee Name: ")
    employee_number = input("Employee Number: ")
    annual_salary = float(input("Annual Salary:$ "))
    annual_bonus = float(input("Annual Bonus:$ "))

    #CREATE A ShiftSupervisor OBJECT
    supervisor = ShiftSupervisor(name, employee_number, annual_salary, annual_bonus)

    # DISPLAY SHIFT SUPERVISOR INFO
    print("\nSHIFT SUPERVISOR INFORMATION:")
    print("NAME:", supervisor.get_employee_name())
    print("EMPLOYEE #:", supervisor.get_employee_number())
    print(f"ANNUAL SALARY: ${supervisor.get_annual_salary(): .2F}")
    print(f"ANNUAL BONUS: ${supervisor.get_annual_production_bonus(): .2F}")
    print(f"TOTAL COMPENSATION: ${supervisor.total_compensation(): .2F}")


#RUN MAIN
if __name__ == "__main__":
    main()