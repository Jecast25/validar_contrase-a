import re

def evaluar_expresion(expresion):
    try:
        if not re.match(r'^[0-9+\-*/().\s]+$', expresion):
            raise ValueError("InvalidExpression")
        resultado = eval(expresion)
        return resultado
    except ZeroDivisionError:
        return "DivisionByZero"
    except Exception as e:
        return f"{str(e)}"
    finally:
        # Limpiar recursos si es necesario
        pass

# Ejemplos de uso
print(evaluar_expresion("3 + 4 * 2"))  # Resultado: 11
print(evaluar_expresion("(10-3) * (2 + 1)"))
print(evaluar_expresion("7/2"))
print(evaluar_expresion("7/0"))
print(evaluar_expresion("7 & 3"))
print(evaluar_expresion("(2 + 3"))
print(evaluar_expresion("5 + 2, 3 * (-2)"))