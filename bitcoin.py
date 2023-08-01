import requests
from twilio.rest import Client
import time

# Configurar las credenciales de Twilio
account_sid = 'ACc98d6ba7f51c7b521b80f15574e7107c'
auth_token = '61c04a7922d0a0faf60ac51d8e0ecd2e'
client = Client(account_sid, auth_token)

# Función para obtener el precio actual del Bitcoin
def get_bitcoin_price():
    url = "https://api.coindesk.com/v1/bpi/currentprice/BTC.json"
    response = requests.get(url)
    data = response.json()
    price = data['bpi']['USD']['rate']
    return price

# Función para obtener el precio actual de Ethereum
def get_ethereum_price():
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "ethereum",
        "vs_currencies": "usd"
    }
    response = requests.get(url, params=params)
    data = response.json()
    price = data['ethereum']['usd']
    return price

# Función para enviar el mensaje de WhatsApp
def send_whatsapp_message(to_number, body):
    message = client.messages.create(
        body=body,
        from_='whatsapp:+14155238886',  # Este es el número proporcionado por Twilio
        to=f'whatsapp:{to_number}'
    )
    print(f"Mensaje enviado a {to_number}: {message.sid}")

# Bucle para enviar el precio del Bitcoin y Ethereum en el mismo mensaje por WhatsApp
while True:
    bitcoin_price = get_bitcoin_price()
    ethereum_price = get_ethereum_price()

    message_body = f"El precio actual del Bitcoin es: {bitcoin_price}\nEl precio actual de Ethereum es: {ethereum_price}"
    recipient_number = '+5491130529469'  # Reemplazar con el número de WhatsApp destinatario

    send_whatsapp_message(recipient_number, message_body)
    time.sleep(1800)  # Esperar 30 minutos antes de enviar la siguiente alerta
