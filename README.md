# Aplicación de Notas para asignaciones

Cuando se cuentan con multiples asignaciones en un equipo de trabajo es necesario llevar un control sobre cada una de las tareas.
Las tareas para ciertos trabajos en específicos, por lo general, cuentan con la siguiente estructura:

- Asignado a
- Titulo
- Contenido
- Estado
- Fecha de inicio
- Fecha de finalización
- Fecha de creación

Mediante el uso de Flask, se tiene el siguiente mini-proyecto para la creación de notas de acuerdo al encargado de asignarlas.

## Indice

- [Aplicación de Notas para asignaciones](#aplicación-de-notas-para-asignaciones)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Instalación del proyecto y sus requerimientos](#instalación-del-proyecto-y-sus-requerimientos)
- [Comando de ejecución del proyecto](#comando-de-ejecución-del-proyecto)

## Tecnologías Utilizadas

- Python: Lenguaje principal del proyecto.
- Flask: Framework para construir endpoints rápidas y modernas.
- flask_sqlalchemy: Validación de datos y creación de modelos.
- SQLite: Base de datos ligera integrada en el proyecto.

## Instalación del proyecto y sus requerimientos

- Clonar repositorio y ubicarnos dentro del proyecto:

```bash
git clone https://github.com/jab9814/notes_app.git
cd notes_app
```

- Crear un entorno virtual (recomendado):

```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

- Instalar dependencias:

```bash
pip install -r requirements.txt
```

## Comando de ejecución del proyecto

Para la ejecución del proyecto es necesario contar con el entorno virtual activo y dentro del proyecto. Ejecutar el siguiente comando:

```bash
flask --app flaskr.app run --debug
```

Obteniendo una url base para iniciar:

```bash
http://127.0.0.1:8000
```

<!-- 
Para ingresar a la consola de Flask, se debe ejecutar el siguiente comando"

```bash
flask --app flaskr.app shell
```

Para interactuar con la app desde la shell de flask, se utiliza:

```bash
    from flaskr.app import db
```
 -->
