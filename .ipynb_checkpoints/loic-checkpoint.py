from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid

def classify(img_path):

    ENDPOINT = "https://projetp8.cognitiveservices.azure.com/customvision/v3.0/Prediction/0f232e41-ae2a-42b3-ad90-a037ae5f9abc/classify/iterations/Iteration1/image"
    prediction_key = "5e7965de387e4b2ea9f3a290b43c511c"
    project_id = "0f232e41-ae2a-42b3-ad90-a037ae5f9abc"
    publish_iteration_name = "Iteration1"
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
    file_location = "\\Users\\maxpl\\Desktop\\SIMPLON\\Projet P8-Triof"

    with open(os.path.join (file_location, img_path), "rb") as image_contents:                                
        results = predictor.classify_image(
            project_id, publish_iteration_name, image_contents.read())
        result = {
            "tag": "",
            "prob": 0
            }

        for prediction in results.predictions:
            if prediction.probability > result["prob"]:
                result["tag"] = prediction.tag_name
                result["prob"] = prediction.probability
        return result


