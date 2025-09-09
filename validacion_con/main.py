import fastapi
from validacion_con.validacion_contraseña import validar_contraseña

app = fastapi.FastAPI()
@app.post("/password/validate")
def validate_password(password: str):
    is_valid, errors = validar_contraseña(password)
    return {"is_valid": is_valid, "errors": errors}
