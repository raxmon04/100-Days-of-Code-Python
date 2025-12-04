from flask import Flask, render_template
import requests

app = Flask(__name__)

data = requests.get("https://api.npoint.io/c790b4d5cab58020d391").json()


@app.route('/')
def home():

    return render_template("index.html", posts=data)


@app.route('/post/<blog_id>')
def read_post(blog_id):

    return render_template("post.html", blog_id=int(blog_id), posts=data)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)