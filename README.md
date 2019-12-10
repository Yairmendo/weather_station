
### Estación de calidad de aire.

**Tabla de  Contenidos**

[TOCM]

[TOC]

#### Objetivo
Tener mayor conciencia de la calidad del aire que respiramos.
Consta de un dispositivo Wemos D1 conectado con sensores de húmedad y de calidad de aire; para poder colocarlo por fuera de la ventana o donde queramos sensar, este dispositivo tiene a su vez una relación maestro-esclavo con la Rasperry Pi la cual va a realizar la conexión a internet y poder realizar su publicación para compartirla en Twitter con la aplicación de desarrollador de twitter.

#### Materiales
- Wemos D1 y Raspberry Pi
- Sensores dht22 (sensor de humedad) y mq135 (sensor de calidad  de aire)
- Adaptadores de energía
- Material de encapsulado(puede ser acrílico) y herramientas de  corte y soldadura electrónica.

#### Configuración inicial de la Rasperry Pi
Dentro del sistema de la Pi,vamos a accesar a un archivo para agregar la red a la que nos vamos a conectar con:

`$ sudo raspi-config`

Después de realizar las conexiones de los sensores a la Wemos D1 vamos a realizar el trámite de ingreso a la API de Twitter para poder publicar la información diariamente. 

#### Conexiones de los sensores a la Wemos D1

La conexión del sensor dht está configurada en el puerto D5 de la Wemos D1 ya que es una salida digital y para el sensor mq135 la salida es a A0 de la Wemos D1. **IMPORTANTE**: Realizar las conexiones a tierra y a 5v adecuadamente deacuerdo a como se puedan acomodar y donde vayan a colocar el dispositivo.

#### Registro en la API de twitter para poder públicar información

Debeos ingresar a la liga https://developer.twitter.com/ Nos registramos y esperamos a que nos den el acceso (usualmente toma 1 día).

#### Agregar los TOKEN y las CONSUMER KEY a nuestro código

Dentro de la rasperry Pi vamos a modificar un archivo que se llama **.profile** , ahí vamos a exportar los dos consumer key tanto la pública como la privada y los token tanto públicos como privados y guardamos, sin dejar espacios copiamos y los pegamos donde corresponden:

```
export CONSUMER_KEY='AQUI VAN'
export CONSUMER_SECRET='AQUI VAN'
export ACCESS_TOKEN='AQUI VAN'
export ACCESS_TOKEN_SECRET='AQUI VAN'
```

ahora instalamos tweepy

con:

`$pip install tweepy`

y vamos a instalar tambien nuestros python requests para hacer los requests a los dispositivos IoT que ya tenemos configurados.

`$sudo apt-get install python-requests`

Ahora vamos a verificar la version de python que tenemos y asegurarnos de que tenemos la versión más actual si no ejecutamos el siguiente comando que va a realizar la descarga de la versión más actualizada IMPORTANTE(Tarda mucho ya que son cerca de 400 test´s)

`$sh pythonversion.sh`

Verificar en el archivo bot.py las direcciones IP de los sensores para que no tengamos problemas donde esta indicado. Importante que el archivo bot.py lo pasemos a la raíz de nuestra Rasperry Pi para que el administrador regular de los procesos que puedan estar en en segundo plano pueda tener acceso al mismo.


#### Modificaciones finales en nuestra Rasperry Pi
Finalmente hacemos ejecutable el archivo con:

`$chmod +x bot.py`

y vamos a poder tener en twitter los datos compartidos de nuestro dispositivo en tiempo real.
