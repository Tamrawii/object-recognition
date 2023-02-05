from imageai.Detection import ObjectDetection
from PyQt5.uic import *
from PyQt5.QtWidgets import QApplication
import os


def recognition():
    model_path = "./Models/yolov3.pt"
    # input_path = "./input/images.jpg"
    input_path = windows.p1.text()
    # output_path = "./output/output_test.jpg"
    output_path = windows.p2.text()

    execution_path = os.getcwd()
    detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(os.path.join(execution_path, model_path))
    detector.loadModel()
    detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path, input_path),
                                                 output_image_path=os.path.join(execution_path, output_path),
                                                 minimum_percentage_probability=30)

    for eachObject in detections:
        print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ", eachObject["box_points"])
        print("--------------------------------")


app = QApplication([])
windows = loadUi("recognition.ui")
windows.show()

windows.b1.clicked.connect(recognition)
app.exec_()
