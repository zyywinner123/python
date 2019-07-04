#coding=utf8
#仅仅提供上传文件服务
import flask
# import make_response
import json
# app = Flask(__name__)
app=flask.Flask(__name__)
@app.route('/upload', methods=['POST', 'GET'])
# @app.route('/', methods=['POST', 'GET'])
def file_upload():

    f = flask.request.files['skFile']#上传的文件名变量为skFile
    f.save("e://flask//"+f.filename);#E盘下需要有flask文件夹
    tt=f.filename
    # image = Image.open(f.filepath)

    # image = cv2.imread("e://flask//"+f.filename)
    # detecotr = TODD()
    # result = detecotr.inputt(image)
    # return '计算的值 ' + str(result)

    response = flask.make_response(json.dumps( tt,default=lambda obj: obj.__dict__, sort_keys=True, indent=4))
    response.headers['Content-Type'] = 'application/json'
    return response
app.run()
if __name__ == '__main__':
    app.run()