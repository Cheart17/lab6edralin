class Person:
    def __init__(self):
        self.name = input("enter name:")
        self.employee_ID = int(input("enter user ID: "))

    def person_info(self):
        print(f"Employee Name: {self.name} \n Employee ID: ")

class Employee(Person):
    def __init__(self):
        super().__init__()
        self.department = input("enter designated department: ")
        self.position = input("enter designated position: ")

    def print_info2(self):
        print(f"User Department: {self.department} \n User Position: {self.position}")

class Salary:
    def __init__(self):
        self.wage_per_hour = float(input("Enter wage per hour: "))
        self.hours_worked_per_day = int(input("Enter Hours worked per day: "))
        self.total_days_in_month = int(input("Enter days worked in the month: "))

    def calculate_total_salary(self):
        calculate = self.wage_per_hour * self.hours_worked_per_day * self.total_days_in_month
        print(f"total Salary: {calculate}")

    def validate_input_wage(self):
            while True:
                try:
                    self.wage_per_hour = float(input("Enter Wage per hour: "))
                    if self.wage_per_hour <= 0:
                        print("please enter a valid input: ")
                    else:
                        print("Validated")
                        break
                except ValueError:
                    print("please input a float or integer number: ")

    def validate_input_hours(self):
        while True:
            try:
                self.hours_worked_per_day = int(input("Enter hours worked per day: "))
                if self.hours_worked_per_day >= 0:
                    if self.hours_worked_per_day <= 24:
                        print("Validated")
                        break
                    else:
                        print("please input a number from the range of numbers 0 - 24")
            except ValueError:
                print("Value Error, Enter a number...")

    def validate_input_days(self):
        while True:
            try:
                self.total_days_in_month = int(input("Enter total day worked in a month: "))
                if self.total_days_in_month >= 0:
                    if self.total_days_in_month <= 31:
                        print("Validated")
                        break
                    else:
                        print("please input a number from the range of numbers 0 - 31")
            except ValueError:
                print("Value Error, Enter a number...")

    def display_salary_info(self):
        calculate = self.wage_per_hour * self.hours_worked_per_day * self.total_days_in_month
        print(f"total Salary: {calculate}")


class Employee1(Person, Employee):
    def __init__(self):
        Person.__init__(self)
        Employee.__init__(self)
        Salary.__init__(self)

    def display_info_method(self):
        self.person_info()
        self.print_info2()
        self.calculate_total_salary()


human1 = Employee1()
human1.display_info_method()