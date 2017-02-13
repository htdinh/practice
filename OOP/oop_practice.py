class Employee:
    'Common base class for all employees'
    empCount = 0  # Share and synchronised among all instances

    @staticmethod
    def get_number_of_employee():  # Class's method  (this method is equivalent to Employee.empCount, but put it in a method way for demonstration)
        return Employee.empCount

    def get_employee_name(self):  # Instance's method, a class can't gene
        return self.name

    def __init__(self, name, salary):
        self.name = name  # Attributes belong only to the instance. No cross-reference among difference instance
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary

print "This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
print "This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

# This is to show that the variable empCount is common for all instance of the
print Employee.empCount, emp1.empCount, emp2.empCount

print Employee.get_number_of_employee(), emp1.get_number_of_employee(), emp2.get_number_of_employee()  # Common to all instances

print emp1.get_employee_name(), emp2.get_employee_name()  # Specific to each instance

print Employee.get_employee_name(emp1), Employee.get_employee_name(emp2)

# print Employee.get_employee_name()   # Throw an error as no instance is specified (to fill in the `self`)
