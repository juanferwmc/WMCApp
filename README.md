# WMCApp

Registro de Pesos de Alambre. 

# Objetivo 
El objetivo de esta aplicación es tener una manera sencilla de poder guardar el peso de los registros que se hacen a cada hora. 

La aplicación va a ser utilizada por los ingenieros de calidad de las plantas y los operadores que realizan los registros, aparte de los directores que ocupen la información. 

Dentro de esta app se pueden registras la siguiente información: Planta, Máquina, Operador, Producto y Peso. Se hizo una investigación utilizando el excel de Productividades de DBPY de cada una de las plantas que fabrican mallas, en este caso son: Beaumont, California, Florida, Illinois y Pennsylvania. 

# Funcionamiento de la App
La app tiene un código de python que está en este repositorio app.py vinculado con streamlit, que es un framework de código abierto en Python que permite scripts en aplicaciones de web abiertas e interactivas. La razón por la que se utiliza streamlit es porque no se necesita conocimiento de CSS, HTML ni otros lenguajes para hacer aplicaciones y es gratuito. 

Los registros proporcionados dentro de la aplicación se mandan a Supabase. Supabase es una página web que funciona como Backend-as-a-Services, en conclusión recibe los registros y los almacena en una base de datos. Dentro de esta base de datos aparte de lo que ya se había comentado hay una columna de fecha_hora que genera el valor exacto en el que se realiza el registro sin importar en que planta se haya hecho el registro. 

# Futuros Acontecimientos
Si en el futuro se necesita agregar un nuevo producto se puede editar el código app.py y poner el nuevo producto o máquina o planta en su respectivo lugar del código. 

Se va a compartir el Streamlit por medio de un URL para que todos los puedan utilizar y se van a compartir el acceso como administrador a quien sea necesario para el funcionamiento de la aplicación, incluyendo Supabase, GitHub y Streamlit. 
