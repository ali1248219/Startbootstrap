from flask import Flask, render_template
import requests
from fetch import Fetch

data_api = requests.get('https://api.npoint.io/76605f216bae8649fb68').json()
data_object = []
for data in data_object:
    data_obj = Fetch(data['id'], data['title'], data['body'], data['subtitle'])
    data_object.append(data_obj)


app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route('/about.html')
def about():
    return render_template('about.html')


@app.route('/contact.html')
def contact():
    return render_template('contact.html')


@app.route('/post/<int:index>')
def posts(index):
    request_post = None
    for data in data_object:
        if data['id'] == index:
            request_post = data
    return render_template('post.html', data=request_post)


if __name__ == "__main__":
    app.run(debug=True)
