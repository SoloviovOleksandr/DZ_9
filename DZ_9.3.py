class Parallelogram:
    def __init__(self, width, length):
        self.width = width
        self.length = length
    def get_area(self):
        return  self.width * self.length
a = Parallelogram(5,6)
print(a.get_area())
class Square(Parallelogram):
    def __init__(self,length):
        super().__init__(length,length)
    def get_area(self):
        return self.length * self.length
b = Square(5)
print(b.get_area())
