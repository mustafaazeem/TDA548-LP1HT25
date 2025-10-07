class employee:
    def __init__(self, name, address, phone_no):
        self.name = name
        self.address = address 
        self.phone_no = phone_no 

    def calculate_salary(self):
        return f'In Super Class'
    

    

class Perm_emp(employee):
    def __init__(self, name, salary, address, phone_no):
        super().__init__(name, address, phone_no)
        self._salary = salary 
    
    def calculate_salary(self):
        return self.salary * 12 
    
    def get_name(self):
        return self.name
    
    @property
    def salary(self):
        print('in a decorated property')
        return self._salary
    
    @salary.setter
    def salary(self, value):
        print('setting new salary')
        self._salary = value
   
class Part_time_emp(employee):
    def __init__(self, name, salary, address, phone_no, emp_rate):
        super().__init__(name, address, phone_no)
        self.salary = salary
        self.emp_rate = emp_rate

    def calculate_salary(self):
        return self.salary * self.emp_rate * 12

class Daily_emp(employee):
    def __init__(self, name, wages, address, phone_no):
        super().__init__(name, address, phone_no)
        self.wages = wages 


def main():
    e1 = Perm_emp('David', 5000, 'Gothenburg', '070 012 89 73')
    e2 = Part_time_emp('Lilly', 2600, 'Partille', '071 118 23 74', .05)

    print(e1.salary)
    e1.salary = 10000 
    print(e1.salary)

    e1._salary = 15000 
    print(e1._salary)
    # e1._salary






main()