#initialize the Salesforce object
import pandas as pd
from simple_salesforce import Salesforce
def setup_connection_salesForce():
    try:
        sf = Salesforce(
        username='Username',
        password='password',
        security_token='',
        sandbox=True)
        print("Connection Successful")
        print(sf)
        return sf
    except Exception as e:
        print("Exception in Connection ",e)
        return None



#querying the object

'''
Note: While using the custom API names, always add the __c at the end of
the object name.
TO change the setting or view the object properties, go to Settings-> Edit the object

'''



def query_salesforce(sf):
    sf_data = sf.query_all("SELECT name,MD5__c,Description__c FROM CRS__c")

    #converting the result into Dataframe
    sf_df = pd.DataFrame(sf_data['records']).drop(columns='attributes')
    print(sf_df)
    return sf_df


def insert_salesforce(sf):
    data = [
      {'Name':'Rakshit456','Description__c':'Test row three','Version__c':'2019203451',
      'MD5__c':'abdbbdbdbdbdbd23u8u8u21','URL__c':'https://avi-portal-s3.s3.amazonaws.com/CrsDownloads/CRS-2019-2-BETA.json?AWSAccessKeyId=AKIAJ2J6EFWYAUAZGNUA&Expires=1597494637&Signature=HRpaJISKlev39go8dVx2d%2FzFy0w%3D',
      'ReleaseDate__c':'2020-11-01'}
    ]
    sf.bulk.CRS__c.insert(data)

def update_salesforce(sf):
     data = [
       {'Name':'Rakshit456','Description__c':'Test row updated'}
     ]
     sf.bulk.CRS__c.update(data)
