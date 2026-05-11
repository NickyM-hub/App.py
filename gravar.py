import firebase_admin
from firebase_admin import credentials, db
import time 
import random

cred = credentials.Certificate("path/to/serviceAccountKey.json")
firebase_admin.initialize_app(cred)

firebase_admin.initialize_app(cred, {'databaseURL': 'https://senac-2b959-default-rtdb.firebaseio.com/'})

ref = db.reference('lab46')

while True:
    dados = {
        "temperatura": round(random.uniform(24, 32), 2),
        "umidade": round(random.uniform(50, 80), 2)
    }

    ref.push(dados)

    print("Enviando: ", dados)

    time.sleep(5)