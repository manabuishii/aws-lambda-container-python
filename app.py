import json
import datetime


# def lambda_handler(event, context):
def handler(event, context):
    param1 = 0
    param2 = 0
    # event['queryStringParameters']['param1']
    if 'queryStringParameters' in event.keys():
        if "param1" in event['queryStringParameters'].keys():
            param1 = int(event['queryStringParameters']['param1'])
        if "param2" in event['queryStringParameters'].keys():
            param2 = int(event['queryStringParameters']['param2'])
    # bodyにデータがある場合            
    # if "param1" in event.keys():
    #     param1 = "param1 is not empty"

    dt_now = datetime.datetime.now()

    return {
        'isBase64Encoded': False,
        'statusCode': 200,
        'headers': {"Access-Control-Allow-Origin": "*"},
        'body': '{"result": '+str(param1*param2)+',"now": "'+ dt_now.isoformat()+'"'+'}'
    }