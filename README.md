# Servidor de pruebas del sistema de telemetría

Implementación de un servidor de prueba muy sencillo para conectar con él el sistema de telemetría desarrollado en la práctica 3 de Usabilidad y Análisis de Juegos. Está implementado en Python y Flask y guarda en un fichero las trazas que se van enviando.

Es necesario Python 3 para poder ejecutarlo:

- Instalar los requisitos con `pip install -r requirements.txt``
- Ejecutar con `python app/main.py`

El servidor queda a la escucha en `localhost:8080`. Hay un punto de acceso con el que enviar nuevas trazas y ver las trazas almacenadas:

- GET `localhost:8080/tracker`: devuelve una lista con las trazas almacenadas
- POST `localhost:8080/tracker`: almacena la cadena de la traza en el servidor. La traza se envía en formato JSON, en un objeto con el siguiente aspecto:

```
{
    "data": "..."
}
```


