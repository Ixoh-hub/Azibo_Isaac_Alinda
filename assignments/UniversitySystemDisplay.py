from abc import ABC, abstractmethod

#Parent class
class Person(ABC):
    def __init__(self, name, age):
        self._name = name
        self._age = age
    
    def getName(self):
        return self._name
    
    def getAge(self):
        return self._age
    
    def displayDetails(self):
        pass

#Subclass 
class Parent(Person):
    def __init__(self, name, age, child_name):
        super().__init__(name, age)
        self._child_name = child_name
        
    def getChildName(self):
        return self._child_name
    
    def displayDetails(self):
        print(f"Parent|Name: {self.getName()}, Age: {self.getAge()}, Child: {self.getChildName()}")

# Subclass
class Student(Person):
    def __init__(self, name, age, course, year):
        super().__init__(name, age)
        self._course = course
        self._year = year
    
    def displayDetails(self):
        print(f"Student|Name: {self.getName()}, Age: {self.getAge()}, Course: {self._course}, Year: {self._year}")

# Sub class     
class Lecturer(Person):
    def __init__(self, name, age, department, salary):
        super().__init__(name, age)
        self._department = department
        self._salary = salary
    
    def displayDetails(self):
        print(f"Lecturer|Name: {self.getName()}, Age: {self.getAge()}, Department: {self._department}, Salary: {self._salary}")
        
# Sub Class
class Staff(Person):
    def __init__(self, name, age, position, salary):
        super().__init__(name, age)
        self._position = position
        self._salary = salary
    
    def displayDetails(self):
        print(f"Staff|Name: {self.getName()}, Age: {self.getAge()}, Position: {self._position}, Salary: {self._salary}")
        
if __name__ == "__main__":
    p = Parent("Mr.Jew", 45, "Desmond")
    s = Student("Desmond", 25, "Software Engineering", 3)
    l = Lecturer("Dr.Joab", 67, "Networks", 2000000)
    t = Staff("Mr.Apitta", 34, "Admin", 1000000)
    
    p.displayDetails()
    s.displayDetails()
    l.displayDetails()
    t.displayDetails()