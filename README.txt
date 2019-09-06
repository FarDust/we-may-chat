# iic2173-E0-base
Repositorio para la Entrega 0

Deben dejar sus servidores corriendo para ser revisados en cualquier momento, hasta que indiquemos que pueden bajarlos

# Que debe ir en el repo

* Configuracion de nginx: nginx.conf y el contenido de la carpeta sites-enabled
* Codigo del servicio web
* Metodo de acceso al servidor. Despues de la revision podran revocar los accesos que nos pasen. Esto puede ser:
  * Llave PEM
  * Llave con passphrase
  * Acceso via usuario - password
  
# Que debe ir aqui

* ass.tralmor.com
* Entrar a la pagina principal, ingresar mensaje en el primer input apretar enter. Luego para ser feliz puedes tipear un nickname en la casilla de abajo. De vez en cuando un chiste de chuk norrris aparecera pues no pude grabar audio con angular :cry:
* Referencias
  - stackoverflow
  - DigitalOcean
---

El funcionamiento de la aplicacion es sencillo, django sirve los archivos estaticos, maneja los templates y gestiona la base de datos en sqlite. La aplicacion en angular compilada en produccíon se conecta al middleware de socket.io en la ruta /socket.io/ y asi se envian los mensajes donde django guarda el contenido de los mensajes y el nickname y emite a los subscriptores un mensaje de respuesta a traves de los sockets abiertos.