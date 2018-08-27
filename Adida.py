#仅仅提供上传文件服务
from flask import Flask , make_response, request,json
# app = Flask(__name__)
app=Flask(__name__)
@app.route('/upload', methods=['POST', 'GET'])
def file_upload():

    f = request.files['skFile']
    f.save("e://flask//"+f.filename);
    tt=f.filename
    # image = Image.open(f.filepath)

    # image = cv2.imread("e://flask//"+f.filename)
    # detecotr = TODD()
    # result = detecotr.inputt(image)
    # return '计算的值 ' + str(result)

    response = make_response(json.dumps( tt,default=lambda obj: obj.__dict__, sort_keys=True, indent=4))
    response.headers['Content-Type'] = 'application/json'
    return response
app.run()
# if __name__ == '__main__':
#     app.run()