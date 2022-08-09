import requests
import time

api_url = "http://localhost:3000/"


# requesting ls command execution
topic_name = "topic_one"
topic_uuid = "fist_message_topic_one"
socket = {"param": "one"}
response = requests.post(api_url + "topic_name/" + topic_name + "/topic_uuid/" + topic_uuid, json=socket)
time.sleep(1)

response = requests.get(api_url + "topic_name/topic_result")
print("Result of topic_one computation:")
print(response.json())



# requesting ps command execution
topic_name = "topic_two"
topic_uuid = "fist_message_topic_two"
socket = {"param": "one"}
response = requests.post(api_url + "topic_name/" + topic_name + "/topic_uuid/" + topic_uuid, json=socket)
time.sleep(1)
response = requests.get(api_url + "topic_name/topic_result")
print("Result of topic_two computation:")
print(response.json())





