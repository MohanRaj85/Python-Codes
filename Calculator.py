
try:
    class Calculator:

        print("Hello Welcome To My Simple Calculator!")

        def __init__ (self,a,b,c):
            self.a = float(input("Enter a Number : "))
            self.b = float(input("Enter a Number : "))
            self.c = input("add/sub/mul/div : ").lower()

            if self.c == "add":
                print(self.a + self.b)

            elif self.c == "sub":
                    print(self.a - self.b)

            elif self.c == "mul":
                print(self.a * self.b)

            elif self.c == "div":
                print(self.a / self.b)
                
            else:
                print("Invalid Operation")

except ValueError as e:
    print(e)
    print("Enter a Number Not a Letter")

except ZeroDivisionError as e:
    print(e)
    print("There is no number is divided by 0!")
    

obj = Calculator(1,2,"add")
