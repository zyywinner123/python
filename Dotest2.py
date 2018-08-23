
# coding:utf8
import os
import sys
import cv2
import numpy as np
import tensorflow as tf
sys.path.append("..")

from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util

from flask import Flask , make_response, request,json


class TOD(object):
    def __init__(self):
        self.MODEL_NAME= 'E:\\111111\herpesV1\com.test\graph'
        # Path to frozen detection graph. This is the actual model that is used for the object detection.
        self.PATH_TO_CKPT = self.MODEL_NAME + '/frozen_inference_graph.pb'

        # List of the strings that is used to add correct label for each box.
        self.PATH_TO_LABELS = os.path.join('E:\\111111\herpesV1\com.test\data', 'herpes_label_map.pbtxt')

        self.NUM_CLASSES = 1

        self.detection_graph = self._load_model()
        self.category_index = self._load_label_map()

    def _load_model(self):
        detection_graph = tf.Graph()
        with detection_graph.as_default():
            od_graph_def = tf.GraphDef()
            with tf.gfile.GFile(self.PATH_TO_CKPT, 'rb') as fid:
                serialized_graph = fid.read()
                od_graph_def.ParseFromString(serialized_graph)
                tf.import_graph_def(od_graph_def, name='')
        return detection_graph

    def _load_label_map(self):
        label_map = label_map_util.load_labelmap(self.PATH_TO_LABELS)
        categories = label_map_util.convert_label_map_to_categories(label_map, max_num_classes=self.NUM_CLASSES, use_display_name=True)
        category_index = label_map_util.create_category_index(categories)
        return category_index

    def detect(self, image):
        with self.detection_graph.as_default():
            with tf.Session(graph=self.detection_graph) as sess:
                # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
                image_np_expanded = np.expand_dims(image, axis=0)
                image_tensor = self.detection_graph.get_tensor_by_name('image_tensor:0')
                # Each box represents a part of the image where a particular object was detected.
                boxes = self.detection_graph.get_tensor_by_name('detection_boxes:0')
                # Each score represent how level of confidence for each of the objects.
                # Score is shown on the result image, together with the class label.
                scores = self.detection_graph.get_tensor_by_name('detection_scores:0')
                classes = self.detection_graph.get_tensor_by_name('detection_classes:0')
                num_detections = self.detection_graph.get_tensor_by_name('num_detections:0')
                # Actual detection.
                (boxes, scores, classes, num_detections) = sess.run(
                    [boxes, scores, classes, num_detections],
                    feed_dict={image_tensor: image_np_expanded})
                # Visualization of the results of a detection.
                vis_util.visualize_boxes_and_labels_on_image_array(
                    image,
                    np.squeeze(boxes),
                    np.squeeze(classes).astype(np.int32),
                    np.squeeze(scores),
                    self.category_index,
                    use_normalized_coordinates=True,
                    line_thickness=8)

        print(np.squeeze(scores)[0])  # 第一个检测区域的识别分数,>0.5可判断为异常
        return np.squeeze(scores)[0]
        # cv2.namedWindow("detection", cv2.WINDOW_NORMAL)
        # cv2.imshow("detection", image)
        # cv2.waitKey(0)

app = Flask(__name__)

@app.route('/upload', methods=['POST', 'GET'])
def file_upload():
    print(request.files)
    print(request.form)
    print(request.args)
    print(request.values)
    print(request.values.get('asda'))
    print(request.values.get('aa'))

    f = request.files['skFile']
    f.save("e://flask//"+f.filename);

    # image = Image.open(f.filepath)

    image = cv2.imread("e://flask//"+f.filename)
    detecotr = TOD()
    result = detecotr.detect(image)
    return '计算的值 ' + str(result)

    user = User('bbb', 456)
    response = make_response(json.dumps(user, default=lambda obj: obj.__dict__, sort_keys=True, indent=4))
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    app.run()

# if __name__ == '__main__':
#     image = cv2.imread("E:\\111111\herpesV1\com.test\\testimage\pi.jpg")
#     detecotr = TOD()
#     detecotr.detect(image)
