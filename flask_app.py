from flask import Flask, render_template, request
import os, shutil
from generate_absent import find_missing

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/upload-files", methods=['GET', 'POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    print("\nTarget folder = ", target)

    if not os.path.isdir(target):
        os.mkdir(target)

    file_list = request.files.getlist("file")
    print("file_list = ", file_list)

    for file in file_list:
        print("\nFile = ", file)

        destination = "/".join([target, file.filename])
        print("\nDestination = ", destination)
        file.save(destination)

    return render_template('absent.html')

@app.route("/displayresults", methods=['GET', 'POST'])
def displayresults():
    result = find_missing()
    print("\nFLASK APP RESULT = ", result)
    path = os.path.join(APP_ROOT, "images")
    shutil.rmtree(path)
    return render_template("result.html", result=result)

if __name__ == '__main__':
    app.run(debug=True)

