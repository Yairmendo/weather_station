# Importamos paquetes que necesitamos
import os
import tweepy
import requests
import time
import datetime

# Obtener las llaves de la app de Twitter desde variables de entorno por seguridad
consumer_key = os.environ.get('CONSUMER_KEY')
consumer_secret = os.environ.get('CONSUMER_SECRET')
access_token = os.environ.get('ACCESS_TOKEN')
access_token_secret = os.environ.get('ACCESS_TOKEN_SECRET')

# Autenticar utilizando estas llaves
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)

# Configura el access token
auth.set_access_token(access_token, access_token_secret)

# Obtiene objeto de API de consulta de twitter
api = tweepy.API(auth)

# Consulta los datos del sensor en la IP del Wemos
response = requests.get('http://dirección IP de los dispositivos')
response2 = requests.get('http://dirección IP de los dispositivos')

# Setup del timestamp 
t = time.time()
timegood = datetime.datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S')

# Convierte la respuesta del servidor de Wemos en un diccionario de Python
sensor_data = response.json()
sensor_data2 = response2.json()

temperature = sensor_data['variables']['temperature']
humidity = sensor_data['variables']['humidity']
pollution = sensor_data['variables']['contaminacion']

temperature2 = sensor_data2['variables']['temperature']
humidity2 = sensor_data2['variables']['humidity']
pollution2 = sensor_data2['variables']['contaminacion']

# Hace el promedio de las mediciones
avtemp = ((temperature+temperature2/2)) 
avhumi = ((humidity+humidity2)/2)
avpoll = ((pollution+pollution2)/2)

# Envia el tweet en mi cuenta
api.update_status('Soy un bot creado por PON TU NOMBRE AQUI \n La temperatura es: {0} ℃ \n La humedad es: {1} %% RH \n La concentración es: {2} %% PPM \n {3}' .format(avtemp, avhumi, avpoll, timegood))
