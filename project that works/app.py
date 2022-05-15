import json
import firebase_admin

from firebase_admin import credentials, firestore, storage

from flask import Flask, render_template, request

cred = credentials.Certificate("custd-89037-firebase-adminsdk-m9pyz-518a531784.json")
firebase_admin.initialize_app(cred, {'storageBucket': 'custd-89037.appspot.com'})

db = firestore.client()
bucket = storage.bucket()

app = Flask(__name__)

@app.route("/")
def main():
    return render_template('main.html')


@app.route("/index")
def index():
    return render_template('index.html')


@app.route("/pic", methods=["POST"])
def pic():
    # if request.method == "GET":
    #     print(request.get_json())
    if request.method == "POST":
        print(request.form['title'])
        title = request.form['title']
        f = request.files['image']
        f.save(title)
        ######## Файл#######
        blob = bucket.blob(title)
        blob.upload_from_filename(title)
        blob.make_public()
        plink= blob.public_url
        #######db#############3
        info = {'title': title, 'image': plink}
        db.collection('pInfo').document().add(info)
        print(request.files["image"])
    return json.load({1: 0})


if __name__ == "__main__":
    app.run(debug=True)
