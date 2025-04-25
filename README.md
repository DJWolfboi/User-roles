Flask Roles and Authentication System

Este es un sistema básico de autenticación con Flask, utilizando roles y permisos para gestionar el acceso de usuarios a diferentes rutas. El proyecto incluye un sistema de login con validación de usuario, roles (administrador y usuario) y la protección de rutas según el rol del usuario autenticado.

Características

Autenticación de usuarios: Los usuarios pueden iniciar sesión con un nombre de usuario y contraseña.

Roles y permisos: Los usuarios pueden tener diferentes roles (por ejemplo, administrador y usuario) y el acceso a rutas específicas se basa en esos roles.

Rutas protegidas: Se implementaron rutas que solo pueden ser accesibles por usuarios autenticados o con roles específicos.

Flask-Login: Manejo de sesiones para usuarios autenticados.

Flask-Principal: Control de accesos según roles y permisos.

Requisitos

Para ejecutar este proyecto, necesitarás tener Python instalado. Además, debes instalar las siguientes dependencias:
```plaintext
pip install -r requirements.txt
```

Instalación y Ejecución

1. Clonar el repositorio:

```
git clone https://github.com/DJWolfboi/User-roles.git
cd FLASK_ROLES_AUTH
```

2. Instalar dependecias:
```plaintext
   pip install -r requirements.txt
```

3. Ejecutar la aplicacion Flask:
   ```plaintext
   python app.py
   ```

4.Acceder a la aplicación:

Abre tu navegador y ve a:

http://127.0.0.1:5000

5.Rutas disponibles:

/login: Página de inicio de sesión.

/dashboard: Página protegida para usuarios autenticados.

/admin: Página solo accesible por administradores.

/logout: Cierra la sesión del usuario.

Pruebas
Para probar el sistema de autenticación, puedes usar las siguientes credenciales de prueba:

Administrador:

Nombre de usuario: DJWolfboi

Contraseña: admin1234

Usuario regular:

Nombre de usuario: Noel

Contraseña: user1234

Diagrama del flujo de autenticación
Se incluye un diagrama de flujo que representa el proceso de autenticación y autorización en la aplicación. El diagrama muestra cómo el usuario ingresa sus credenciales, si son correctas, se otorgan permisos y se redirige al dashboard o a la página de administración.

Contribuciones
Si deseas contribuir al proyecto, por favor sigue los siguientes pasos:

1.Haz un fork de este repositorio.

2.Crea una nueva rama para tus cambios.

3.Realiza tus cambios y haz un commit.

4.Abre un pull request con una descripción clara de los cambios realizados.
