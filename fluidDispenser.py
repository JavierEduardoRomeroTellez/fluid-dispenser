from gpiozero import Button
from gpiozero import LED
from time import sleep
import requests
import json

button1 = Button(19)
pump = LED(26)
verde = LED(6)
rojo = LED(17)


url = 'http://dev.relred.com/soldix/api/transactions'


while True:
    user = input('Scan QR\n')
    payload = { 'u_id': user, 'p_id': 'p6368e1c90d9bc' }
    response = requests.post(url, json=payload)
    print(response.url)
				
    if response.status_code == 200:
        result = response.json()
        if result['message'] == 'SUCCESS':
            verde.on()
            button1.wait_for_press()
            verde.off()
            pump.on()
            sleep(7)
            pump.off()
        if result['message'] == 'FAIL':
            rojo.on()
            sleep(2)
            rojo.off()
            continue
