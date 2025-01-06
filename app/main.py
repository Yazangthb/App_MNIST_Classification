from flask import Flask, request, jsonify

from app.torch_utils import transform_image, get_prediction

app = Flask(__name__)

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}
def allowed_file(filename):
    # something.png
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        if file is None or file.filename == '':
            return jsonify({'result': 'no file'})
        if not allowed_file(file.filename):
            return jsonify({'result': 'not supported format'})
                           
        try:
            im_bytes = file.read()
            tensor = transform_image(im_bytes)
            prediction = get_prediction(tensor)
            data = {'prediction': prediction.item(), 'class_name': str(prediction.item())} #class name here is just a demonstration, would be usefull in CIFAR for example
            return jsonify(data)
        except:
            return jsonify({'result': 'error during prediction'})
        
    # 1 load image
    # 2 image -> tensor
    # 3 prediction
    # 4 return json
    return jsonify({'result': 1})