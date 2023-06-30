import pickle
import pandas as pd
import numpy  as np

class HealthInsurance():
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
        gender_encoding = pd.get_dummies(data['Gender'], prefix='Gender')

        # Gender
        if 'Gender_Female' in gender_encoding:
            data['Gender_Female'] = gender_encoding['Gender_Female']

        if 'Gender_Male' in gender_encoding:
            data['Gender_Male'] = gender_encoding['Gender_Male']

        # Driving License
        if 'Driving_License_0' in driving_license_encoding:
            data['Driving_License_0'] = driving_license_encoding['Driving_License_0']

        if 'Driving_License_1' in driving_license_encoding:
            data['Driving_License_1'] = driving_license_encoding['Driving_License_1']

        # Previously Insured
        if 'Previously_Insured_0' in previously_insured_encoding:
            data['Previously_Insured_0'] = previously_insured_encoding['Previously_Insured_0']

        if 'Previously_Insured_1' in previously_insured_encoding:
            data['Previously_Insured_1'] = previously_insured_encoding['Previously_Insured_1']

        # VehicleDamage
        if 'Vehicle_Damage_Yes' in vehicle_damage_encoding:
            data['Vehicle_Damage_Yes'] = vehicle_damage

        cols_drop = ['id','Gender','Driving_License','Previously_Insured','Vehicle_Damage']
        data = data.drop( cols_drop, axis=1 )

        return data
    
    def get_prediction( self, model, original_data, test_data ):
        # model prediction
        pred = model.predict_proba( test_data )

        # join prediction into original data
        original_data['score'] = pred[:, 1].tolist()
        
        return original_data.to_json( orient='records', date_format='iso' )
