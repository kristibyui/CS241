"""
CS241 Team Activity 07
Written by Chad Macbeth
"""

from abc import ABC
from abc import abstractmethod

### Abstract Class for common attributes of any employee
class Employee(ABC):

   ### Initialize the Employee object
   def __init__(self):
      self.name = ""

   ### Display the employee 
   @abstractmethod
   def display(self):
      print(self.name)

   ### Determine the paycheck amount
   @abstractmethod
   def get_paycheck():
      pass


### Hourly Employee that derives from the Employee base class
### Must implement display and get_paycheck
class HourlyEmployee(Employee):

   ### Initialize the hourly employee object
   def __init__(self):
      self.hourly_wage = 0.0
      self.hours = 0.0

   ### Display the employee
   def display(self):
      print("{} - ${:.2f}/hour" .format(self.name, self.hourly_wage))

   ### Paycheck is based on wage and number of hours worked
   def get_paycheck(self):
      return self.hourly_wage * self.hours


### Salary Employee that derives from the Employee base class
### Must implement display and get_paycheck
class SalaryEmployee(Employee):

   ### Initialize the salary employee object
   def __init__(self):
      self.salary = 0.0

   ### Display the employee
   def display(self):
      print("{} - ${:.2f}/year" .format(self.name, self.salary))

   ### Paycheck is based on being paid twice a month
   def get_paycheck(self):
      return self.salary / 24.0

### Display employee information including name, pay details, and
### paycheck amount.  This demonstrates polymorphisim.
def display_employee_data(employee):
   employee.display()
   print("Payheck ${:.2f}" .format(employee.get_paycheck()))

### Provide menu to keep track of a list of employees
def main():
   employees = []
   selection = ""
   while selection != "q":
      print("Menu")
      print("h) Add hourly")
      print("s) Add salary")
      print("q) Quit")
      selection = input("> ")
      if selection == "h":
         employee = HourlyEmployee()
         employee.name = input("Name: ")
         employee.hourly_wage = float(input("Hourly Rate: "))
         employee.hours = float(input("Hours: "))
         employees.append(employee)
      elif selection == "s":
         employee = SalaryEmployee()
         employee.name = input("Name: ")
         employee.salary = float(input("Salary: "))
         employees.append(employee)
   print()
   for employee in employees:
      display_employee_data(employee)

if __name__ == "__main__":
   main()
