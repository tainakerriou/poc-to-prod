from flask import Flask, request, render_template

from predict.predict.run import TextPredictionModel

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('template.html')


@app.route("/", methods=['POST'])
def get_prediction():
    model = TextPredictionModel.from_artefacts("train/data/artefacts/saved_models/2023-01-06-17-55-58")
    text = request.form['text']
    predictions = model.predict([text], top_k=1)

    return str(predictions)


@app.route("/predict", methods=["GET"])
def request_prediction():
    model = TextPredictionModel.from_artefacts("train/data/artefacts/saved_models/2023-01-06-17-55-58")
    text = request.args.get('text')
    predictions = model.predict([text], top_k=1)

    return str(predictions)

if __name__ == '__main__':
    app.run(debug=True)