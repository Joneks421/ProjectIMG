import firebase_admin

from firebase_admin import credentials, firestore, storage

import json
info = {
  "id": "aba23fc0-1008-11e8-b8b2-2b0fbff0de7d",
  "title": "Макет дизайна",
  "url": "https://storage.googleapis.com/neto-api.appspot.com/pic/aba23fc0-1008-11e8-b8b2-2b0fbff0de7d/bMFAlDwf9AI.jpg",
  "mask": "https://www.googleapis.com/download/storage/v1/b/neto-api.appspot.com/o/pic%2F8ece7a20-15f4-11e8-96fd-2513ea9afcae-mask.png?generation=1519100719825524&alt=media",
  "timestamp": 1518449006013,
  "comments": {
    "-L59YakIzQIO4_qiP6ws": {
      "left": 100,
      "message": "Тут мне кажется лучше подойдет розовый цвет",
      "timestamp": 1518448045157,
      "top": 65
    },
    "-L59bM_rv4fesvnQ1nts": {
      "left": 953,
      "message": "Эта картинка на коллаже слишком шумная",
      "timestamp": 1518449031562,
      "top": 480
    }
  },
}
cred = credentials.Certificate("custd-89037-firebase-adminsdk-m9pyz-518a531784.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'custd-89037.appspot.com'})

db = firestore.client()
############ Загрузка Файла########
fileN = 'pnglol.jpg'
bucket = storage.bucket()
blob = bucket.blob(fileN)
blob.upload_from_filename(fileN)
blob.make_public()

print(blob.public_url)

############Добавление инфы в БД##########3
db.collection('pInfo').add(info)
########Чтение################3
# result = db.collection('pInfo').get() Чтение всего катлога
# result = db.collection('pInfo').document("docname").get() Чтение Только одного документа

#
# for i in result:
#     print(i.to_dict())
