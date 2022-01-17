import os
import numpy as np
from flask import Flask, render_template, request
import joblib
from PIL import Image
import glob
import cv2
import tensorflow as tf
from keras.models import model_from_json


app = Flask(__name__)

store_File = ""

img_Dir = 'E:/AI-ML-Images/'


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/receive_data', methods=["POST", "GET"])
def receive_data():
    image_Filename = ""
    for img_File in os.listdir(img_Dir):
        image_Filename = img_File

    image = cv2.imread(img_Dir + image_Filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
    new_img = tf.keras.utils.normalize(resized, axis=1)
    new_img = np.array(new_img).reshape(-1, 28, 28, 1)
    json_file = open('model.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")
    prediction = loaded_model.predict(new_img)
    print(np.argmax(prediction))
    predicted_Output = np.argmax(prediction)
    return render_template('predict.html', predicted=predicted_Output)


@app.route('/shape_predict')
def shape_predict():
    return render_template("shapes.html")


@app.route('/receive_shape', methods=["POST", "GET"])
def receive_shape():
    image_Filename = ""
    for img_File in os.listdir(img_Dir):
        image_Filename = img_File

    image = cv2.imread(img_Dir + image_Filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    resized = cv2.resize(gray, (28, 28), interpolation=cv2.INTER_AREA)
    new_img = tf.keras.utils.normalize(resized, axis=1)
    new_img = np.array(new_img).reshape(-1, 28, 28, 1)
    json_file = open('model_shapes.json', 'r')
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model_shapes.h5")
    prediction = loaded_model.predict(new_img)
    print(np.argmax(prediction))
    predicted_Output = np.argmax(prediction)
    return render_template('predict.html', predicted=predicted_Output)

    # return "Hello"


    # print("Hello")


if __name__ == "__main__":
    app.run(debug=True, port=8080)


# model = joblib.load("draw.joblib")
