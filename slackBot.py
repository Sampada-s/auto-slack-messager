import json
import requests

def lambda_handler(event, context):
    mentionList = ['<@user1>','<@user2','<@user3']
    mentions = ''.join(mentionList)
    message = f"Hi {mentions} please see this message"
    send_message_to_slack(message)
    return {
        'message': 'Lambda function run succesfully'
    }

def send_message_to_slack(text):

    post = {"text": f"{text}"}

    try:
        json_data = json.dumps(post)
        req = request.Request("incomingHook",
                              data=json_data.encode('ascii'),
                              headers={'Content-Type': 'application/json'}) 
        r = request.urlopen(req)
    except Exception as em:
        print("EXCEPTION: " + str(em))