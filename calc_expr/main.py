import fastapi
from calculadora_expresiones import evaluar_expresion

app = fastapi.FastAPI()
@app.post("/calculate")
def calculate_expression(expression: str):
    return {"result": evaluar_expresion(expression)}