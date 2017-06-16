from flask import Flask
from flask import request
from subprocess import check_output
app = Flask(__name__)
 
@app.route("/", methods=['GET', 'POST'])
def rosette():
    return check_output(["/bin/bash","ros", request.form['text']])
 
if __name__ == "__main__":
    app.run()
