#from azure.cognitiveservices.vision.customvision.training import CustomVisionTrainingClient
from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
#from azure.cognitiveservices.vision.customvision.training.models import ImageFileCreateBatch, ImageFileCreateEntry, Region
from msrest.authentication import ApiKeyCredentials
import os, time, uuid


path = "Images/gobelet.jpg"
def first_prediction_azure(path):
    
    #ENDPOINT = "https://projet8-prediction.cognitiveservices.azure.com/"
    ENDPOINT = "https://projetp8.cognitiveservices.azure.com/customvision/v3.0/Prediction/0f232e41-ae2a-42b3-ad90-a037ae5f9abc/classify/iterations/Iteration1/image"
    prediction_key = "5e7965de387e4b2ea9f3a290b43c511c"
    project_id = "0f232e41-ae2a-42b3-ad90-a037ae5f9abc"
    publish_iteration_name = "Iteration1"
    prediction_resource_id = "/subscriptions/9b9c4a7a-4f40-4fc2-ab99-0bbe0c4064bd/resourceGroups/GR_Amirouche/providers/Microsoft.CognitiveServices/accounts/projet8"
    
    # Test du point de terminaison
    prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
    predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)
    
    #base_image_location = "\Users\maxpl\Desktop\SIMPLON\Projet P8 - Triof"
    base_image_location = "/Users/maxpl/Desktop/SIMPLON/Projet P8 - Triof"
    # base_image_location = "base_image_location = "/mnt/c/Documents and Settings/flore/OneDrive/Documents/Simplon/Rendus_projets_Florent/Projet_en_cours/Projet P8 - Triof/triof/"
    #publish_iteration_name = "model1"
    #project_id="66b07b7d-03ff-4c7e-9892-9d854e949ad0"
    resultat = ""
    print(os.path.join(base_image_location, path))
    
    with open(os.path.join(base_image_location, path), "rb") as image_contents:
        results = predictor.classify_image(
            project_id, publish_iteration_name, image_contents.read())
        
        for prediction in results.predictions:
        #print("\t" + prediction.tag_name +
             # ": {0:.2f}%".format(prediction.probability * 100))
            if (results.predictions[0].probability > results.predictions[1].probability) or (results.predictions[0].probability > results.predictions[2].probability):
                resultat = results.predictions[0].tag_name
            elif results.predictions[1].probability > results.predictions[0].probability or (results.predictions[1].probability > results.predictions[2].probability):
                resultat = results.predictions[1].tag_name
            else:
                resultat = results.predictions[2].tag_name
                
    return print(resultat)

first_prediction_azure(path)