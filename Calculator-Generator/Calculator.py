def add(n1,n2):
     return(n1+n2)

def subtract(n1,n2):
     return n1 - n2

def multiply(n1,n2):
     return  n1 * n2

def divide(n1,n2):
    return n1 / n2

operations = {
     '+': add,
     '-': subtract, 
     '*' : multiply,
     '/' : divide
} 

def cal():
        num1 = int(input("what's the first number?\n"))

        for symbol in operations:
            print(symbol)
        should_continue = True

        while should_continue:

            operation_symbol = input("Pick an operation: ")

            num2 = int(input("what's the next number?:"))

            calculation = operations[operation_symbol]
            answer = calculation(num1,num2)

            print(f"{num1} {operation_symbol} {num2} = {answer}")

            if input(f"Type 'y' to continue with {answer} or type 'n' to start.: " ).lower() == 'y':
                num1 = answer
            else:
                should_continue = False
                cal()
cal()
