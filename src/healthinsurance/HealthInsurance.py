import pickle
import pandas as pd
import numpy  as np

class HealthInsurance( object ):
    def __init__( self ):
        self.home_path = ''
        self.annualpremiums_scaler       = pickle.load( open( self.home_path + 'parameter/annual_premium_scaler.pkl', 'rb' ) )
        self.regioncode_scaler           = pickle.load( open( self.home_path + 'parameter/region_code_scaler.pkl', 'rb' ) )
        self.policysaleschannel_scaler   = pickle.load( open( self.home_path + 'parameter/policy_sales_channel_scaler.pkl', 'rb' ) )
        self.age_scaler                  = pickle.load( open( self.home_path + 'parameter/age_scaler.pkl', 'rb' ) )
        self.vintage_scaler              = pickle.load( open( self.home_path + 'parameter/vintage_scaler.pkl', 'rb' ) )
      
    def data_preparation( self, data ):
        # Annual_Premium
        data['Annual_Premium'] = self.annualpremiums_scaler.transform( data[['Annual_Premium']].values )

        # Region_Code
        data['Region_Code'] = self.regioncode_scaler.transform( data[['Region_Code']].values )

        # Policy Sales Channel
        data['Policy_Sales_Channel'] = self.policysaleschannel_scaler.transform( data[['Policy_Sales_Channel']].values )

        # Age
        data['Age'] = self.age_scaler.transform( data[['Age']].values )

        # Vintage
        data['Vintage'] = self.vintage_scaler.transform( data[['Vintage']].values )

        # Gender - one hot encoding
        time_mapping_gender = {'Female': 0, 'Male': 1}
        data['Gender'] = data['Gender'].map(time_mapping_gender)

        # Vehicle Age - ordinal
        time_mapping_vage = {'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2}
        data['Vehicle_Age'] = data['Vehicle_Age'].map(time_mapping_vage)

        # Vehicle_Damage
        time_mapping_vda = {'No': 0, 'Yes': 1}
        data['Vehicle_Damage'] = data['Vehicle_Damage'].map(time_mapping_vda)

        return data
    
    def get_prediction(self, model, original_data, test_data):
        # model prediction
        pred = model.predict_proba( test_data )[:,1]

        # join prediction into to original data
        original_data['prediction'] = pred

        return original_data.to_json( orient = 'records', date_format ='iso' )
