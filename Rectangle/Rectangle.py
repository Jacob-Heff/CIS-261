# Jacob Heffington
# CIS261
# Rectangle

class Rectangle:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def perimeter(self):
        p = (self.height*2)+(self.width*2)
        return p
    
    def area(self):
        a = self.height*self.width
        return a
    
    def rectPrint(self):
        for i in range(self.height):
            if i == 0 or i == self.height - 1:
                print('* ' * self.width)
            else:
                print('* ' + '  ' * (self.width - 2) + '* ')

def main():
    while True:
        print("Rectangle Calculator\n")
        h = int(input("Height:     "))
        w = int(input("Width:      "))
        rect = Rectangle(h, w)
        
        print("Perimeter: ", rect.perimeter())
        print("Area:      ", rect.area())
        rect.rectPrint()
        
        fb = input("\nContinue? (y/n)").lower()
        if fb != "y":
            return None
        
main()