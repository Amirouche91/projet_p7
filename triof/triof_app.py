from flask import Flask, render_template, request
from src.utils import *

from ../prediction import *
import cv2
from base64 import b64encode
from PIL import Image
import numpy as np
from io import BytesIO

import os
import random
from matplotlib.image import imread

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

"""
@app.route('/start')
def insert():
    open_waste_slot()
    
    return render_template('insert.html')
"""

@app.route('/start')
def insert():
    open_waste_slot()
    paths = os.listdir('Images/Test')
    path = random.choice(paths)
    pics = take_trash_picture(path)
    prediction = first_prediction_azure('test/'+path)
    PIL_image = Image.fromarray(np.uint8(pics)).convert('RGB')
    data = BytesIO()
    PIL_image.save(data, "JPEG")
    data64 = b64encode(data.getvalue())
    PIL_image = u'data:img/jpeg;base64,'+data64.decode('utf-8') 
    return render_template('insert.html', pics = PIL_image, prediction = prediction)


@app.route('/waste/pick-type')
def pick_type():
    close_waste_slot()

    return render_template('type.html')


@app.route('/confirmation', methods=['POST'])
def confirmation():
    waste_type = request.form['type']

    process_waste(waste_type)
    return render_template('confirmation.html')


if __name__ == "__main__":
    app.run(debug=True)

