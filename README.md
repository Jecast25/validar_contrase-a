# Validador de Contraseñas

Este proyecto es un **validador de contraseñas** que utiliza Python para verificar si una contraseña cumple con ciertos criterios de seguridad. Los criterios incluyen una longitud mínima, la presencia de mayúsculas, minúsculas, dígitos y caracteres especiales, y la ausencia de espacios.

-----

## Cómo Ejecutar
Antes de ejecutar la aplicación se necesita instalar las dependencias que están descritas em el archivo "requirements.txt"


Para ejecutar la aplicación, necesitas tener **Python** y **FastAPI** instalados. Sigue estos pasos:

1.  Asegúrate de tener Python instalado. Si no es así, descárgalo de la [página oficial de Python](https://www.python.org/).

2.  Instala FastAPI y Uvicorn (el servidor web) utilizando pip:

    ```bash
    pip install "fastapi[all]" uvicorn
    ```

3.  Ejecuta la aplicación desde la línea de comandos:

    ```bash
    uvicorn main:app --reload
    ```

La API estará disponible en `http://127.0.0.1:8000`.

-----

## Cómo Correr Pruebas

Para probar el endpoint de la API, puedes usar una herramienta como `cURL` o un cliente de API como **Postman**.

### Con cURL

Abre una nueva terminal y envía una solicitud POST con una contraseña:

```bash
curl -X POST "http://127.0.0.1:8000/password/validate" \
     -H "Content-Type: application/json" \
     -d '{"password": "MiContraseñaSegura123!"}'
```

Reemplaza `"MiContraseñaSegura123!"` por la contraseña que quieras validar. El resultado te indicará si la contraseña es válida y, de no serlo, por qué.