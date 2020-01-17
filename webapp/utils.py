import pandas as pd
from simple_salesforce import Salesforce
def setup_connection_salesForce():
    try:
        sf = Salesforce(
        username='sfsbservice@avinetworks.com.sandeep',
        password='blahblah4',
        security_token='',
        sandbox=True)
        print("Connection Successful")
        print(sf)
        return sf
    except Exception as e:
        print("Exception in Connection ",e)
        return None
