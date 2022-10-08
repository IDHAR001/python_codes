class EmployeeController:
    def __init__(self) -> None:
        self.employees = []

    def add_employee(self,employee):
        self.employees.append(employee)
        
    def total_salary(self):
        total_salary = 0
        for item in self.employees:
            total_salary += item.total_salary()
        return total_salary
    
class Employee:
    def total_salary(self):
        raise ValueError("没用子类工资")

class Salesman(Employee):
    def __init__(self,base_salary,sales) -> None:
        super().__init__()
        self.base_salary = base_salary
        self.sales = sales
    
    def total_salary(self):
        return self.base_salary+self.sales*0.05

class Programmer(Employee):
    def __init__(self,base_salary,bonus) -> None:
        super().__init__()
        self.base_salary = base_salary
        self.bonus = bonus
        
    def total_salary(self):
        return self.base_salary+self.bonus

p01 = Programmer(2000,200)
s01 = Salesman(100,10000)
c01 = EmployeeController()
c01.add_employee(p01)
c01.add_employee(s01)
print(p01.total_salary())
print(s01.total_salary())
print(c01.total_salary())