import io
import base64
import numpy as np
import tensorflow as tf
import logging

from io import BytesIO
from PIL import Image
from flask import Flask, request, render_template, redirect

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)

model = tf.keras.models.load_model('model/v1/retinal-oct.h5')
model_v2 = tf.keras.models.load_model("./model/v2/retinal_oct_v2.h5")

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

def allowed_file(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS

def prepare_image(img):
    """
    prepares the image for the api call
    """
    img = Image.open(io.BytesIO(img)).convert('RGB')
    img = img.resize((150, 150))
    img = np.array(img)
    img = np.expand_dims(img, 0)
    return img

def predict_result(img):
    """predicts the result"""
    return np.argmax(model.predict(img)[0])

def prepare_image_v2(img):
    img = img.resize((150, 150))
    img = np.stack((img,)*3, axis=-1)
    img = np.expand_dims(img, 0)
    return img

def predict_result_v2(img):
    with tf.device("/CPU:0"):
        Y_pred = model_v2.predict(img)
    predicted_class = np.argmax(Y_pred, axis=1)
    predicted_probability = Y_pred[0][predicted_class[0]] * 100
    return class_labels[predicted_class[0]], predicted_probability

class_labels = {
    0: "CNV",
    1: "DME",
    2: "DRUSEN",
    3: "NORMAL"
}


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

# Route originale de l'API
@app.route("/predict", methods=["POST"])
def infer_image():
    logging.info(str(request.files))
    
    # Catch the image file from a POST request
    if "file" not in request.files:
        return "Please try again. The Image doesn't exist"
    
    file = request.files.get("file")
    
    if not file:
        return

    # Read the image
    img_bytes = file.read()

    # Prepare the image
    img = prepare_image(img_bytes)

    # Return on a JSON format
    return str(predict_result(img))

@app.route("/predict_v2", methods=["GET", "POST"])
def predict_v2():
    if request.method == "POST":
        if "files[]" not in request.files:
            return redirect(request.url)

        images = []
        for file in request.files.getlist("files[]"):
            if allowed_file(file.filename):
                img_str = base64.b64encode(file.read()).decode("utf-8")
                img = Image.open(BytesIO(base64.b64decode(img_str)))
                images.append((img_str, img))

        predictions = [(img_str, *predict_result_v2(prepare_image_v2(img))) for img_str, img in images]
        return render_template("index.html", predictions=predictions, class_labels=class_labels)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
