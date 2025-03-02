from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/success', methods=['GET'])
def success():
    return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)