import sys,os
from ecosortvision.pipeline.training_pipeline import TrainPipeline
from ecosortvision.utils.main_utils import decodeImage, encodeImageIntoBase64
from flask import Flask, request, jsonify, render_template,Response
from flask_cors import CORS, cross_origin
from ecosortvision.constants.application import APP_HOST, APP_PORT


app = Flask(__name__)
CORS(app)

class ClientApp:
    def __init__(self):
        self.filename = "inputImage.jpg"



@app.route("/train")
def trainRoute():
    obj = TrainPipeline()
    obj.run_pipeline()
    return "Training Successfull!!" 



#DEFAULT ROUTE
@app.route("/")
def home():
    return render_template("index.html")


# #PREDICTION ROUTE(sir)
# @app.route("/predict", methods=['POST','GET'])
# @cross_origin()
# def predictRoute():
#     try:
#         image = request.json['image']
#         decodeImage(image, clApp.filename)

#         os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source ../data/inputImage.jpg")

#         opencodedbase64 = encodeImageIntoBase64("yolov5/runs/detect/exp/inputImage.jpg")
#         result = {"image": opencodedbase64.decode('utf-8')}
#         os.system("rm -rf yolov5/runs")

#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside  json data")
#     except KeyError:
#         return Response("Key value error incorrect key passed")
#     except Exception as e:
#         print(e)
#         result = "Invalid input"

#     return jsonify(result)



#PREDICTION ROUTE(Mine)


@app.route("/predict", methods=['POST','GET'])
@cross_origin()
def predictRoute():
    try:
        image = request.json['image']
        decodeImage(image, clApp.filename)

        os.system(
            "yolo predict "
            "model=artifacts/model_trainer/best.pt "
            "source=data/inputImage.jpg "
            "conf=0.5 "
            "save=True "
            "project=runs/detect "
            "name=prediction "
            "exist_ok=True"
        )

        opencodedbase64 = encodeImageIntoBase64(
            "runs/detect/runs/detect/prediction/inputImage.jpg"
        )

        result = {"image": opencodedbase64.decode('utf-8')}

        # Optional cleanup
        # os.system('rm -rf runs')

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")

    except KeyError:
        return Response("Key value error incorrect key passed")

    except Exception as e:
        print(e)
        result = "Invalid input"

    return jsonify(result)


# @app.route("/live", methods=['GET'])
# @cross_origin()
# def predictLive():
#     try:
#         os.system("cd yolov5/ && python detect.py --weights my_model.pt --img 416 --conf 0.5 --source 0")
#         os.system("rm -rf yolov5/runs")
#         return "Camera starting!!" 

#     except ValueError as val:
#         print(val)
#         return Response("Value not found inside  json data")
    



@app.route("/live", methods=['GET'])
@cross_origin()
def predictLive():
    try:

        os.system(
            "yolo predict "
            "model=artifacts/model_trainer/best.pt "
            "source=0 "
            "conf=0.5 "
            "show=True"
        )

        return "Camera starting!!"

    except ValueError as val:
        print(val)
        return Response("Value not found inside json data")




if __name__ == "__main__":
    clApp = ClientApp()
    app.run(host=APP_HOST, port=APP_PORT)
