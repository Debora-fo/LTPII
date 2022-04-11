'''- Uma classe abstrata deve herdar de ABC (Abstract Base Classes)

- Analise o problema do empregado e o cálculo do seu salário.

- A superclasse Employee representa um funcionário em tempo integral ou por hora.
A classe Employee deve ser uma classe abstrata porque existem apenas funcionários
em tempo integral e funcionários horistas, não existem empregados gerais.
A classe Employee deve ter um método concreto que retorne o nome completo de
um funcionário. Além disso, deve ter um método que calcule o salário. O método
cálcula salário deve ser um método abstrato.

Implemente:
1- A classe Employee com os atributos first_name e Last_name
- O Construtor e os métodos gets e sets
- O método concreto full_name
- O métod abstrato compute_salary
5- Um objeto da classe Employee
- A classe FulltimeEmployee com os atributos first_name, Last_name e salary
- O Construtor e os métodos gets e sets
- A RN(Regra de Negócio) do salário é o salário fixo mais um bônus de 200 reais
- Um objeto da classe FulltimeEmployee
- A classe HourlyEmployee com os atributos first_name, Last_name, worked_hours, rate
- O Construtor e os métodos gets e sets
- A RN do salário é worked_hours vezes rate
- Um objeto da classe HourlyEmployee

- A classe Payroll com o atributo employee_list
- O construtor não recebe nada e o método get_employee_list
- O método add para adicionar um empregado a lista
- Adicione os obejtos criados (os empregados) a lista de Payroll
- O método print_payroll que mostra a folha de pagamento com o nome completo e
o salário do funcionário.

Prof. Barbosa

'''
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_first_name(self):
        return self.first_name
    def get_last_name(self):
        return self.last_name

    def set_first_name(self,new_first_name):
        self.first_name = new_first_name

    def set_last_name(self,new_last_name):
        self.last_name = new_last_name

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @abstractmethod
    def compute_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self, salary, first_name, last_name):
        super().__init__(first_name, last_name)
        self.salary = salary

    def get_salary(self):
        return self.salary

    def set_salary(self,new_salary):
        self.salary = new_salary

    def compute_salary(self):
        rn_full = self.salary + 200
        print('Salário:',rn_full)
        return rn_full

class HourlyEmployee(Employee):
    def __init__(self,worked_hours,rate,first_name,last_name):
        super().__init__(first_name, last_name)
        self.worked_hours = worked_hours
        self.rate = rate

    def get_worked_hours(self):
        return self.worked_hours
    def get_rate(self):
        return self.rate

    def set_worked_hours(self,new_worked_hours):
        self.worked_hours = new_worked_hours
    def set_rate(self,new_rate):
        self.rate = new_rate

    def compute_salary(self):
        rn_hourly = self.worked_hours * self.rate
        print('Salário:', rn_hourly)
        return rn_hourly

class Payroll():
    def __init__(self):
        self.employee_list = list()

    def add_employee(self,employee):
        self.employee_list.append(employee)

    def print_payroll(self):
        print('Folha de pagamento:')
        for e in self.employee_list:
            print(f"{e.full_name()}\t${e.compute_salary()}")

if __name__ == '__main__':
    empregado2= FulltimeEmployee(2000,'Bilbo','Bolseiro')
    empregado3 = HourlyEmployee(40,100,'Nicolas','Cage')
    folha = Payroll()
    print('------------------------------------------')
    empregado2.full_name()
    empregado2.set_last_name('Teste')
    empregado2.full_name()
    empregado2.compute_salary()
    empregado2.set_salary(5000)
    empregado2.compute_salary()
    print('------------------------------------------')
    empregado3.full_name()
    empregado3.compute_salary()
    print('------------------------------------------')
    print(folha.employee_list)
    folha.add_employee(empregado2)
    folha.add_employee(empregado3)
    print(folha.employee_list)
    print('------------------------------------------')
    # folha.print_payroll(empregado2)
    folha.print_payroll()










