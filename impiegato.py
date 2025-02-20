class Employee:
    def __init__(self, nome, cognome, salario):
        self.nome = nome
        self.cognome = cognome
        self.salario = salario
    
    def __repr__(self):
        return f"Employee: {self.nome} {self.cognome}, Salario: {self.salario}"

class Manager(Employee):
    def __init__(self, nome, cognome, salario, reparto):
        super().__init__(nome, cognome, salario)
        self.reparto = reparto  
    
    def __repr__(self):
        return f"Manager: {self.nome} {self.cognome}, Reparto: {self.reparto}, Salario: {self.salario}"

employee = Employee("Christian", "Paperi", 2000)
manager = Manager("Lorenzo", "Scavolini", 3500, "Marketing")

print(employee) 
print(manager)