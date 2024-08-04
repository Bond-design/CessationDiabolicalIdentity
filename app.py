from flask import Flask, send_from_directory

app = Flask(__name__)

@app.route('/')
def index():
    return send_from_directory('static', 'index.html')

@app.route('/download')
def download_book():
    return send_from_directory('static', 'Cessation_of_the_Diabolical_Identity.pdf')

if __name__ == '__main__':
    app.run(debug=True)


