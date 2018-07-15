from flask import Flask, request
from keras.models import Sequential
from keras.layers import Dense
from keras.models import model_from_yaml
import json
import numpy as np
import itertools
import pandas as pd
import tensorflow as tf

app = Flask(__name__)

req = ""

#import tensorflow as tf
yaml_file = open('model.yaml', 'r')
loaded_model_yaml = yaml_file.read()
yaml_file.close()
loaded_model = model_from_yaml(loaded_model_yaml)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])

@app.route("/is_dab", methods=['POST'])
def is_dab():
    print("method called")
    #print(request)
    data = request.get_json()
    data = data["dab_data"]
    #print(data[0])
    merged = list(itertools.chain.from_iterable(data))
    merged = list(itertools.chain.from_iterable(merged))
    #print(merged)
    merged = [round(float(x),2) for x in merged]
    data2 = np.array(merged)
    df = pd.DataFrame(data2)
    #print(len(df))
    df = np.array(df).T
    #print(df.shape)
    #df = np.reshape(1,126)
    #loaded_model._make_predict_function()
    #global graph = tf.get_default_graph()
    ans = loaded_model.predict(df)
    ans = str(ans)
    print(ans)
    return ans

if __name__ == '__main__':
"app.py" 53L, 1401C            
