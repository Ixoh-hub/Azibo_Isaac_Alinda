#METHOD OVERRIDING USING QUADRILATERALS

class Quadrilateral:
    def Perimeter(self):
        print("Add all sides")
    
class Rectangle(Quadrilateral):
    def Perimeter(self):
        print("2(Length+Width)")

class Square(Quadrilateral):
    def Perimeter(self):
        print("4(Side)")

A = Quadrilateral()
B = Rectangle()
C = Square()

A.Perimeter()
B.Perimeter()
C.Perimeter()