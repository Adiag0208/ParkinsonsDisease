# flask, scikit-learn, pandas, pickle-mixin

import pandas as pd
from flask import Flask, render_template, request

app = Flask(__name__)
# data = pd.read_csv('parkinsons.csv')

@app.route('/')
def index():

    models = ["SVM", "Linear Regression", "Decision Tree", "ANN"]

    print(models)
    return render_template('index.html', models=models)

if __name__ == "__main__":
    app.run(debug=True, port=5500)