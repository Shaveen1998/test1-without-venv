from flask import Flask
from keras.models import load_model
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import Dense, LSTM


app = Flask(__name__)

@app.route('/train', methods=['POST'])
def train():
    return'Training completed successfully'

if __name__ == '__main__':
    app.run()

