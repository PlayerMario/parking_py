# PARKING PY
Proyecto de gestión de un Parking, desarrollado en Python.

## Tecnología y lenguaje utilizado:
Para el desarrollo de la aplicación, se han utilizado los siguientes elementos:
- **Python** para el desarrollo del código de gestión de la aplicación.
- **Pickle** como tipo de fichero para la persistencia de los datos.

## Entorno de desarrollo y ejecución:
Para el desarrollo del proyecto, se ha utilizado el entorno de desarrollo **PyCharm**. Para su ejecución, tendremos que elegir un intérprete, en este caso,
durante el dessarrollo, se ha utilizado Python 3.10. Tras ello, se seleccionará en la barras superior, en la parte derecha, el archivo **main.py** como archivo
de ejecución.
A la hora de ejecutar el proyecto, en el archivo **main.py**, entre las líneas de código 24 y 28, podemos seleccionar reiniciar la base de datos para que se pongan
los datos de prueba que hay en el archivo **data.py**, o utilizar los datos guardados en la base de datos por la persistencia de la misma.

## Pruebas:
Para poder probar el proyecto, tendremos distintas opciones:
- **Zona Cliente**: Accederemos a realizar funciones como cliente. En este caso, podremos depositar un vehículo como cliente ocasional o abonado (si estamos dados
  de alta como tal), o retirarlo de la misma forma.
- **Zona Admin**: Necesitaremos un usuario y contraseña, en este caso, **admin-1234**. Una vez dentro, podremos ver el estado del parking, comprobar la facturación 
  de clientes no abonados entre las fechas que indiquemos, consultar los datos de todos los abonados que existen en la base de datos, dar de alta, modificar o dar 
  de baja abonados, y comprobar la caducidad de los abonados en un mes concreto o en los próximos 10 días a partir de hoy.
- **Base Datos**: Podremos comprobar los datos que hay guardados en ese momento en la base de datos para ver ejemplos de clientes ocasionales, abonados, ver el estado
  de todas las plazas, los cobros, cobros de abonados y las plazas que están reservadas.

## Organización del proyecto:
En la carpeta principal nos encontramos con **src**, que es la carpeta donde se aloja todo el código fuente utilizado en el desarrollo de la aplicación.