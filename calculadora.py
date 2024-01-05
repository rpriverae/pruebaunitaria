#calculadora.py
def suma(a, b, c):
    return a + b + c

def resta(a, b):
    return a - b

def multiplicacion(a, b, c):
    return a * b * c

def division(a, b):
    if b != 0:
        return a / b
    else:
        raise ValueError("No se puede dividir por cero")