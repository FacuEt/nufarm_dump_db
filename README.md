#Install Python
```
[Python >= 3.7](https://www.python.org/downloads/)
```

#Install dependencies: 
```
pip3 install firebase-admin google-cloud-firestore pandas

```

#Generate services key and put this in file ```credentials/nufarmServiceAccountKey.json```

#Execute
```
python3 dumpDB.py
```

#Output: the script generate dump file in ```dumps/nufarm_dump_DATE.csv```