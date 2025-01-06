# MNIST Classification Application via Flask and Heroku

This repository contains an application for classifying handwritten digits using the MNIST dataset. It provides code for both a Flask-based API for prediction and training scripts for building the classification model.


# Features

- **Prediction API**: Flask API for predicting handwritten digits from uploaded images.
- **Pretrained Model**: A simple neural network trained on the MNIST dataset.
- **Model Training**: Script to train the MNIST classifier from scratch.

---

# Usage (Heroku)
1. Clone the repository:
   ```bash
   git clone https://github.com/Yazangthb-App_MNIST_Classification.git
   cd Yazangthb-App_MNIST_Classification
2. create and activate a virtual environment, visit [this webpage][https://flask.palletsprojects.com/en/stable/installation/#installation] for details.
4. install requirements.txt
   ```bash
   pip install -r requirements.txt
   
5. install Heroku and login via cmd, visit [this webpage][https://www.heroku.com/] for details.
6. Create a Heroku app and run it
   ```bash
   heroku create <your_app_name>
   heroku local
   git init
   heroku git:remote -a <your_app_name>
   git add .
   git commit -m "initial commit"
   git push heroku master
8. test your application via test.py, don't forget to change the link in the code to your new heroku application link
   ```bash
   cd test
   python test.py

# Usage (Local)
1. Clone the repository:
   ```bash
   git clone https://github.com/Yazangthb-App_MNIST_Classification.git
   cd Yazangthb-App_MNIST_Classification
   
2. create and activate a virtual environment, visit [this webpage][https://flask.palletsprojects.com/en/stable/installation/#installation] for details.
   
4. install requirements.txt
   ```bash
   pip install -r requirements.txt

   
5. change the import names
   
app.torch_untils to torch_utils in main.py,

and PATH = "app\\mnist_ff.pth" to PATH = "mnist_ff.pth" in torch_utils.py


8. Start you flask app
   ## on Windows:
   ```bash
   cd app
   $env:FLASK_APP = "main.py"
   $env:FLASK_ENV = "development"
   flask run
   ```
   ## on linux/MacOS:
   ```bash
   cd app
   export FLASK_APP = main.py
   export FLASK_ENV = development
   flask run

5. test your application via test.py
   ```bash
   cd test
   python test.py

