from flask import Flask, render_template

app = Flask(__name__, template_folder="C:/Git/100-Days-of-Code-Python/056_RenderingHTML")

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)