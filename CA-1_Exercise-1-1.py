#
import re
import datetime

class EmployeeDetails:

    # Using regex expression
    r_int = '^[0-9]*$'
    r_char = r"[\sa-zA-Z]+$"
    r_char_int = "^[0-9A-Za-z]*$"

    # Check user input as a number
    def numbercheck(message):
        while True:
            try:
                value = float(input(message))
            except ValueError:
                print("Invalid Input, Please re-enter the correct value")
                continue
            else:
                return value

    # Check user input for employee name
    while True:
        employee_name = input('Employee Name: ')
        if not re.match(r_char,employee_name) or re.match(r_int,employee_name) or employee_name.strip()=='':
            print('Please enter a valid employee name in charecter format')
            continue
        else:
            break

    # Check user input for employee name
    while True:
        employee_num = input('Employee Number: ')
        if not re.match(r_char_int,employee_num):
            print('Please enter a valid employee number')
            continue
        else:
            break

    # Check user input for week ending
    while True:
        week = input('Week ending: ')
        try:
            datetime.datetime.strptime(week,"%d/%m/%Y")
            break
        except ValueError:
            print('Invalid Input, please use DD/MM/YYYY format')
            continue

    # Entering hours worked from user
    hours_worked = numbercheck("Number of hours worked: ")

    # Get rate per hour from user
    hourly_rate = numbercheck('Enter hourly rate: ')

    # Check user input for over time rate
    if hours_worked > 37.5:
        overtime_rate = numbercheck('overtime_rate Rate: ')
    else:
        overtime_rate = 0

    # Check user input for normal tax rate
    while True:
        standard_taxrate = numbercheck('Standard Tax Rate: ')
        if standard_taxrate >= 100:
            print('Invalid Input, Please re-enter')
            continue
        else:
            break

    # Check user input for Overtime tax rate
    while True:
        overTax = 0
        if hours_worked > 37.5:
            overTax = numbercheck('Overtime Tax Rate: ')
            if overTax >= 100:
                print('Invalid Input, Please re-enter')
                continue
            else:
                break
        break

    # Calculate earnings for standard working hours
    def earningCalculation(self):
        self.earning = 0
        if self.hours_worked >= 37.5:
            self.earning = 37.5 * self.hourly_rate
            return self.earning
        else:
            self.earning = self.hours_worked * self.hourly_rate
            return self.earning

    # Calculate tax on Overtime earnings
    def calculateOvertimeRate(self):
        self.over_time = 0
        self.over_time_rate = 0
        if self.hours_worked > 37.5:
            self.over_time = self.hours_worked - 37.5
            self.hours_worked = 37.5
            self.over_time_rate = self.over_time * self.overtime_rate
            return self.over_time_rate
        else:
            return 0

    # Calculate tax on standard earnings
    def taxdeductionCalculation(self):
        self.tax = (self.earning * self.standard_taxrate)/100
        return self.tax

    # Calculate tax on Overtime earnings
    def overtimeratetaxCalculation(self):
        self.otax = 0
        if self.overtime_rate > 0:
            self.otax =  (self.over_time_rate * self.overTax)/100
            return self.otax
        else:
            return 0

    # Calculating total earnings
    def earningTotal(self):
        self.total = 0
        if self.hours_worked > 37.5:
            self.total = self.earning + self.over_time_rate
            return self.total
        else:
            self.total = self.earning
            return self.total

    # Calculating total tax on earnings
    def taxTotal(self):
        self.taxTotal = 0
        if self.hours_worked >= 37.5:
            self.taxTotal = self.tax + self.otax
            return self.taxTotal
        else:
            self.taxTotal = self.tax
            return self.taxTotal

    # Calculating net payment after tax deductions
    def netPayment(self):
        self.netpay = 0
        if self.hours_worked >= 37.5:
            self.netpay = self.total - self.taxTotal
            return self.netpay
        else:
            self.netpay = self.earning - self.tax
            return self.netpay

    # Creating payslip
    def showPayslip(self):
        print("\n\t\t\t\t\t\t\t\tPAYSLIP\n");
        print('WEEK ENDING ',self.week)
        print('Employee: ',self.employee_name)
        print('Employee Number: ',self.employee_num)
        print('\t\t\t\t\t\tEarnings\t\t\t\t\t\t\t\tDeduction')
        print('\t\t\t\t\t\tHours\t\t\tRate\t\t\tTotal')
        print('Hours (normal)\t\t\t',self.hours_worked,'\t\t\t',self.hourly_rate,'\t\t',self.earning,'Tax @',self.standard_taxrate,'%',self.tax)
        print('Hours (overtime rate)\t\t', self.over_time, '\t\t\t', self.overtime_rate, '\t\t', self.over_time_rate, 'Tax @',self.overTax,'%', self.otax)
        print('\n\t\t\t\tTotal Pay:\t\t\t\t\t\t\t\t\t',self.total)
        print('\t\t\t\tTotal deduction:\t\t\t\t\t\t\t',self.taxTotal)
        print('\t\t\t\tNet pay:\t\t\t\t\t\t\t\t\t',self.netpay)

# Initialization of object
e = EmployeeDetails()

# Object calling
e.earningCalculation()
e.calculateOvertimeRate()
e.taxdeductionCalculation()
e.overtimeratetaxCalculation()
e.earningTotal()
e.taxTotal()
e.netPayment()
e.showPayslip()
