class Multiplication:
    def product(self, x, y=1, z=1):
        return x*y*z

A = Multiplication()
print(A.product(5, 5))
print(A.product(5, 7, 9))