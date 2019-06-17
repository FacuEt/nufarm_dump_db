import firebase_admin
from firebase_admin import credentials, firestore
import pandas as pd
from datetime import datetime

print("INIT Nufarm dump DB script")

PATH_BASE = "dumps"

cred = credentials.Certificate("credentials/nufarmServiceAccountKey.json")
firebase_admin.initialize_app(cred)

print("Firestore configuration success")

store = firestore.client()
doc_ref = store.collection(u'registros')

registros = []

print("Waiting for registers processing")
try:
	docs = doc_ref.get()
	i = 1
	for doc in docs:
		print("processing register number: " + str(i))
		registro = doc.to_dict()
		registro.update({"id": doc.id})
		registros.append(registro)
		i = i + 1
except google.cloud.exceptions.NotFound:
	print(u'Error: Missing data')

print("Registers processed")

df = pd.io.json.json_normalize(registros, sep='.')
file_path = PATH_BASE + '/nufarm_dump_'+ datetime.now().strftime("%d-%m-%Y_%H-%M-%S")  +'.csv'
df.to_csv(file_path, header=True, index=False)

print("Finish, csv saved in " + file_path)
