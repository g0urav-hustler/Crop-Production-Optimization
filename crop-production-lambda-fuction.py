import os
import boto3 

ENDPOINT_NAME = os.environ['ENDPOINT_NAME']
runtime = boto3.client('runtime.sagemaker')
def lambda_handler(event, context):
    label_dict = {0: 'Apple', 1: 'Banana', 2: 'Blackgram', 3: 'Chickpea', 
    4: 'Coconut', 5: 'Coffee', 6: 'Cotton', 7: 'Grapes', 8: 'Jute', 
    9: 'Kidneybeans', 10: 'Lentil', 11: 'Maize', 12: 'Mango', 13: 'Mothbeans', 14: 'Mungbean', 15: 'Muskmelon', 
    16: 'Orange', 17: 'Papaya', 18: 'Pigeonpeas', 19: 'Pomegranate', 20: 'Rice', 21: 'Watermelon'}

    test_value = event["data"]
    
    serialised_input = ",".join(map(str,test_value))
  
    response = runtime.invoke_endpoint(EndpointName = ENDPOINT_NAME,
                                      ContentType = 'text/csv',
                                      Body = serialised_input)
                                       
    
    predicted_value = response['Body'].read().decode()
    predicted_value = int(predicted_value.split(".")[0])
    
    
    return label_dict[predicted_value]
