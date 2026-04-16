#Schafer, C. (2016, June 23). Python OOP Tutorial 2: Class Variables [Video]. YouTube

class Employee:
    #pass
    num_of_emps = 0
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last =last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

        Employee.num_of_emps += 1

    def fullname(self): #add self to expect instance
        return '{} {}'.format(self.first, self.last) #be careful on this part!! change from emp to self
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)
print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# print(Employee.num_of_emps)
# emp_1.raise_amount = 1.05
# print(emp_1.__dict__)
# # emp_1.apply_raise()
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


# emp_1.raise_amount
# Employee.raise_amount