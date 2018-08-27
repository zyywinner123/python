from flask import Flask , make_response, request,json,send_file
import os
import time

import cv2
import numpy as np
import tensorflow as tf
import sys
from matplotlib import pyplot as plt
# This is needed since the notebook is stored in the object_detection folder.


sys.path.append("..")

# Import utilites

from object_detection.utils import label_map_util

from object_detection.utils import visualization_utils as vis_util

'''
调用方法的形式，传入照片或者照片地址，只做一次初始化，速度快！！！

'''
class TODD():

    def inputt(self,image):
        frame = cv2.imread(image)
        frame_expanded = np.expand_dims(frame, axis=0)
        grapht = time.time()  # 标记运算开始时间
        # Perform the actual detection by running the model with the image as input
        (boxes, scores, classes, num) = sess.run(
            [detection_boxes, detection_scores, detection_classes, num_detections],
            feed_dict={image_tensor: frame_expanded})

    # Draw the results of the detection (aka 'visulaize the results')
        vis_util.visualize_boxes_and_labels_on_image_array(
            frame,
            np.squeeze(boxes),
            np.squeeze(classes).astype(np.int32),
            np.squeeze(scores),
            category_index,
            use_normalized_coordinates=True,
            line_thickness=2,
            min_score_thresh=0.0002)
        # jishu
        # All the results have been drawn on the frame, so it's time to display it.
        grapht2 = time.time()  # 标记运算结束时间
        print("可能性:", np.squeeze(scores)[0], "运算耗时:", grapht2 - grapht)  # 打印

        if np.squeeze(scores)[0] > 0.00002:

            (r, g, b) = cv2.split(frame)
            herpes = frame
            herpes = cv2.merge([b, g, r])
            #cv2.imwrite(check_name, frame)
            plt.imshow(herpes)
            # plt.pause(1)
            # plt.show()

            markPicUrl = 'e://flask//result.jpg'
            cv2.imwrite(markPicUrl,frame)
            print(type(markPicUrl))
        return np.squeeze(scores)[0],markPicUrl
# if __name__ == '__main__':

MODEL_NAME = 'E:\\111111\herpesV1\com.test\graph'
# MODEL_FILE = MODEL_NAME + '.tar.gz'
# DOWNLOAD_BASE = 'http://download.tensorflow.org/models/object_detection/'
# Path to frozen detection graph. This is the actual model that is used for the object detection.
PATH_TO_CKPT = MODEL_NAME + '/frozen_inference_graph.pb'
# List of the strings that is used to add correct label for each box.
PATH_TO_LABELS = os.path.join('E:\\111111\herpesV1\com.test\data', 'herpes_label_map.pbtxt')
NUM_CLASSES = 1

## Load the label map.
# Label maps map indices to category names, so that when our convolution
# network predicts `5`, we know that this corresponds to `king`.
# Here we use internal utility functions, but anything that returns a
# dictionary mapping integers to appropriate string labels would be fine
label_map = label_map_util.load_labelmap(PATH_TO_LABELS)
categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=NUM_CLASSES,
                                                            use_display_name=True)
category_index = label_map_util.create_category_index(categories)

# Load the Tensorflow model into memory.
tstart = time.time()  # 标记模型初始化开始时间
detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_CKPT, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')

    sess = tf.Session(graph=detection_graph)

tend = time.time()  # 模型初始化结尾时间
print("启动时间:", tend - tstart)  # 打印
# Define input and output tensors (i.e. data) for the object detection classifier

# Input tensor is the image
image_tensor = detection_graph.get_tensor_by_name('image_tensor:0')

# Output tensors are the detection boxes, scores, and classes
# Each box represents a part of the image where a particular object was detected
detection_boxes = detection_graph.get_tensor_by_name('detection_boxes:0')

# Each score represents level of confidence for each of the objects.
# The score is shown on the result image, together with the class label.
detection_scores = detection_graph.get_tensor_by_name('detection_scores:0')
detection_classes = detection_graph.get_tensor_by_name('detection_classes:0')

# Number of objects detected
num_detections = detection_graph.get_tensor_by_name('num_detections:0')
# detecotr = TODD()
# detecotr.inputt("E:\\111111\herpesV1\com.test\\testimage\pi.jpg")
# detecotr.inputt("e://flask//1.JPG")

    # detecotr.input("E:\dev\models-master\\test\\testimage\\000296.jpg")
    # detecotr.input("E:\dev\models-master\\test\\testimage\\000297.jpg")
    # detecotr.input("E:\dev\models-master\\test\\testimage\\000304.jpg")
app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def file_upload():

    f = request.files['skFile']
    # f.save("e://flask//"+f.filename);
    f.save("e://flask//"+"1.jpg");
    tt=f.filename
    # image = Image.open(f.filepath)

    # image = cv2.imread("e://flask//"+f.filename)
    # image = cv2.imread("e://flask//"+"1.jpg")
    detecotr = TODD()
    result = detecotr.inputt("E:\\flask\\1.jpg")
    # return '计算的值 ' + str(result)

    response = make_response(json.dumps(tt, default=lambda obj: obj.__dict__, sort_keys=True, indent=4))#返回数据
    # response.headers['Content-Type'] = 'application/json'
    # response.headers['response'] = str(result)
    # response(f, mimetype='application/octet-stream')
    response = make_response(send_file(result[1]))
    response.headers['result'] = str(result[0])
    response.headers["Content-Disposition"] = "attachment; filename=myfiles.xls;"+tt
    return response
    # return response

if __name__ == '__main__':
    app.run()
