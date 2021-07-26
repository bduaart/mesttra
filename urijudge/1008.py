#Problem name: Salary
#Resolved by: Bruno Duarte
employeeNumber = int(input())
hoursWork = int(input())
valueHour = float(input())

salary = hoursWork * valueHour

print("NUMBER = {}".format(employeeNumber))
print("SALARY = U$ {:.2f}".format(salary))