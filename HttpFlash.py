from flask import Flask , make_response, request,json

app = Flask(__name__)


class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@app.route('/')
def hello_world():
    return 'Hello World'

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
    #
    return 'file uploaded successfully'

    user = User('bbb', 456)
    response = make_response(json.dumps(user, default=lambda obj: obj.__dict__, sort_keys=True, indent=4))
    response.headers['Content-Type'] = 'application/json'
    return response

if __name__ == '__main__':
    app.run()