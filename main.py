# add two numbers 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def divide(x , y):
    return x/y

def multipy(x, y):
    return x*y

result = 0
while True:
    try:
        val1 = float(input("Enter first value: "))

        val2 = float(input("Enter second value "))
        opperation = input("Enter operation( add, subtract, multipy, divide :)")

        match opperation:
            case "add":
                result = add(val1,val2)

            case "subtract":
                result = subtract(val1, val2)  

            case "multiply":
                result = multipy(val1, val2)    

            case "divide":
                result= divide(val1, val2)
        print(result)       
    except ValueError:
        print("Invalid input. Please enter a number. ")
    except ZeroDivisionError:
        print("Cannot devide by zero.")

    if input("Do you want to continue ?(yes/no:) ") != "yes":
        break
