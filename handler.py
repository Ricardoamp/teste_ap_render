import pickle
import pandas as pd
from flask import Flask, request, Response
from healthinsurance.HealthInsurance import HealthInsurance
import os

# loading model
model = pickle.load(open('model/model_health_insurance.pkl','rb') )


# Initialize API
app = Flask(__name__)

@app.route( '/healthinsurance/predict', methods=['POST'] )
def Health_Insurance_Predict():
    test_json = request.get_json()

    if test_json: # se tiver dados
        if isinstance( test_json, dict ): #unique example
            test_raw = pd.DataFrame( test_json, index=[0] )

        else: #multiple example
            test_raw = pd.DataFrame( test_json, columns = test_json[0].keys())
            
        # Instantiate Rossmann class
        pipeline = HealthInsurance()

        # data preparation
        df1 = pipeline.data_preparation( test_raw )

        # prediction
        df_response = pipeline.get_prediction( model, test_raw, df1 )

        return df_response

    else:
        return Response( '{}', status=200, mimetype='application/json' )

if __name__ == '__main__':
    port = os.environ.get( 'PORT', 5000 )
    app.run( host = '127.0.0.1', port = port, debug=True )
