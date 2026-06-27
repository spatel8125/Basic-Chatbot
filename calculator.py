

def calculate(expression):

    try:
        allowed = "0123456789+-*/().% "

        for char in expression:
            if char not in allowed:
                return "Invalid characters found."

        answer = eval(expression)

        return f"Answer = {answer}"

    except ZeroDivisionError:
        return "Error: Division by zero."

    except:
        return "Invalid Expression."