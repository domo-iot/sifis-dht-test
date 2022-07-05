import requests

api_url = "http://localhost:3000/"

#insert Socket
topic_name = "SIFIS::Sockets"
topic_uuid = "FirstSocket"
socket = {"socket_uuid": "FirstSocket", "description": "First DHT Socket", "connected": True}
response = requests.post(api_url + "topic_name/" + topic_name + "/topic_uuid/" + topic_uuid, json=socket)
print(response.json())


#insert Light
topic_name = "SIFIS::Lights"
topic_uuid="FirstLight"
light = {"light_uuid": "FirstLight", "description": "First DHT Light", "connected": True}
response = requests.post(api_url + "topic_name/" + topic_name + "/topic_uuid/" + topic_uuid, json=light)
print(response.json())

# get_all
response = requests.get(api_url + "get_all");
print(response.json())

#get_topic_name
topic_name = "SIFIS::Lights"
response = requests.get(api_url + "topic_name/" + topic_name)
print(response.json())

#get_topic_uuid
response = requests.get(api_url + "topic_name/" + topic_name + "/topic_uuid/" + topic_uuid)
print(response.json())

#publish volatile message
volatile_message = {"message": "hi" }
response = requests.post(api_url + "pub", json=volatile_message)
print(response.json())



