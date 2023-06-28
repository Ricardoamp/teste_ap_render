import pickle
import pandas as pd
import numpy  as np
import json

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
        gender_encoding = pd.get_dummies(data['Gender'], prefix = 'Gender')

        # Driving License - one hot encoding
        driving_license_encoding = pd.get_dummies(data['Driving_License'], prefix = 'Driving_License')

        # Previously Insured - one hot encoding
        previously_insured_encoding = pd.get_dummies(data['Previously_Insured'], prefix = 'Previously_Insured')

        # Vehicle Age - ordinal
        time_mapping = {'< 1 Year': 0, '1-2 Year': 1, '> 2 Years': 2}
        data['Vehicle_Age'] = data['Vehicle_Age'].map(time_mapping)

        # Vehicle_Damage
        vehicle_damage_encoding = pd.get_dummies( data['Vehicle_Damage'], prefix = 'Vehicle_Damage' )

        # Gender
        data['Gender_Female'] = gender_encoding['Gender_Female']
        data['Gender_Male'] = gender_encoding['Gender_Male']

        # Driving License
        data['Driving_License_0'] = driving_license_encoding['Driving_License_0']
        data['Driving_License_1'] = driving_license_encoding['Driving_License_1']

        # Previously Insured
        data['Previously_Insured_0'] = previously_insured_encoding['Previously_Insured_0']
        data['Previously_Insured_1'] = previously_insured_encoding['Previously_Insured_1']

        # VehicleDamage
        data['Vehicle_Damage_Yes'] = vehicle_damage_encoding['Vehicle_Damage_Yes']
        data['Vehicle_Damage_No'] = vehicle_damage_encoding['Vehicle_Damage_No']

        cols_drop = ['Gender','Driving_License','Previously_Insured','Vehicle_Damage']
        data = data.drop( cols_drop, axis=1 )

        return data
    
    def get_prediction(self, model, original_data, test_data):
        # model prediction
        pred = model.predict_proba( test_data )

        # join prediction into to original data
        original_data['prediction'] = pred

        return original_data.to_json( orient = 'records', date_format ='iso' )
