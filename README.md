# 🐍 Proyectos de Python - Primer Año

¡Bienvenido! Este repositorio es una colección de los proyectos, ejercicios y trabajos realizados durante mi primer año de aprendizaje en Python. El contenido abarca desde conceptos básicos de programación estructurada hasta la creación de una aplicación de consola con conexión a una base de datos.

## 📂 Estructura del Repositorio

El contenido está organizado por semestre y por proyectos individuales:

* **`primer_semestre/`**: Contiene ejercicios fundamentales de Python. Aquí se practican conceptos como:
    * Variables y tipos de datos.
    * Operadores aritméticos y lógicos.
    * Estructuras condicionales (`if`, `elif`, `else`).
    * Ciclos (`for`, `while`).

* **`segundo_semestre/`**: Avanza hacia temas más complejos, con un foco en:
    * **Programación Orientada a Objetos (POO):** Clases, objetos, herencia y polimorfismo.
    * Ejercicios prácticos como una calculadora implementada con clases.

* **`crud_escuela/`**: El proyecto más completo del repositorio. Es una aplicación de consola que demuestra la integración de Python con una base de datos MySQL.

---

## ✨ Proyecto Destacado: `crud_escuela`

Esta es una aplicación de consola que simula un sistema de gestión para una escuela. Permite realizar operaciones **CRUD** (Crear, Leer, Actualizar y Eliminar) para las entidades principales de una institución educativa.



[Image of a CRUD operation flow diagram]


### Funcionalidades
* Gestión completa (CRUD) de **Alumnos**.
* Gestión completa (CRUD) de **Profesores**.
* Gestión completa (CRUD) de **Cursos**.

### 🛠️ Cómo Ejecutar `crud_escuela`

Sigue estos pasos para probar la aplicación en tu entorno local.

**1. Prerrequisitos:**
* Tener Python 3 instalado.
* Tener un servidor de base de datos MySQL funcionando.

**2. Configuración de la Base de Datos:**
* Crea una base de datos vacía en tu servidor MySQL.
* Importa el archivo **`escuela.sql`** (que se encuentra en la carpeta del proyecto) para crear las tablas y la estructura necesaria.

**3. Instalar Dependencias:**
Esta aplicación requiere el conector oficial de MySQL para Python. Instálalo usando pip:
```bash
pip install mysql-connector-python
