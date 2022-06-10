from io import BytesIO
import numpy as np
from keras import models
from keras.applications.mobilenet import preprocess_input as preprocessing
from PIL import Image
from flask import jsonify, Flask, request
import h5py
from urllib import request as req
from keras_preprocessing import image


def load_model():
    model_h5 = h5py.File("my_model.h5", "r")
    model = models.load_model(model_h5)
    return model


def image_preprocess_and_predict(img):
    # Preprocess your image here
    model = load_model()
    labels = (['open mouth', 'puff cheek', 'show teeth', 'smile', 'sneer'])

    x = image.img_to_array(img=img)
    x = np.expand_dims(x, axis=0)
    x = preprocessing(x)

    images = np.vstack([x])
    classes = model.predict(images)[0]
    # array_pose = {'open mouth': 0, 'puff cheek': 0,
    #               'show teeth': 0, 'smile': 0, 'sneer': 0}

    array_pose = []
    for (label, p) in zip(labels, classes):
        value = round((p*100), 2)
        array_pose.append({"poseName": label, "value": value})

    # Return image yg udah diolah
    return array_pose


def predict_pose_func(img):
    prediction_result = image_preprocess_and_predict(img)
    return prediction_result


app = Flask(__name__)


@app.route('/', methods=["GET"])
def predict():
    try:
        BASE_URL = "https://storage.googleapis.com/api_face-1/androFrom/"
        FILE_NAME = request.args.get('file')

        url = BASE_URL + FILE_NAME
        res = req.urlopen(url).read()
        img = Image.open(BytesIO(res)).resize((224, 224))
        return jsonify(predict_pose_func(img))
    except Exception as e:
        return f"An Error Occured: {e}"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
