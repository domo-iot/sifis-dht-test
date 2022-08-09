import websocket
import time
import json
import os
import subprocess


SUBSCRIBED_TOPICS = ["topic_one", "topic_two"]

PROGRAM_TO_CALL = {
    "topic_one": "ls",
    "topic_two": "ps"
    }

def execute_command(cmd):
    print("Executing command " + cmd)
    returned_output = subprocess.check_output(cmd)
    output = returned_output.decode("utf-8")
    print(output)
    
    print("RequestPostTopicUUID")
    
    ws_req = {
        "RequestPostTopicUUID": {
            "topic_name": "topic_result",
            "topic_uuid": "topic_result_one",
            "value": {
                "result_string": output
            }
        }
    }
            
    ws.send(json.dumps(ws_req))
    
    

def on_message(ws, message):
    print("Received:")
    print(message)
    
    json_message = json.loads(message)
    
    
    if "Persistent" in json_message:
        json_message = json_message["Persistent"]
        
        if "topic_name" in json_message:
            if json_message["topic_name"] in SUBSCRIBED_TOPICS:
                print("Received instance of " + json_message["topic_name"])
                execute_command(PROGRAM_TO_CALL[json_message["topic_name"]])
            else:
                print("We are not subscribed to this topic")
    

def on_error(ws, error):
    print(error)


def on_close(ws, close_status_code, close_msg):
    print("### Connection closed ###")


def on_open(ws):
    print("### Connection established ###")

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://localhost:3000/ws",
                                on_open=on_open,
                                on_message=on_message,
                                on_error=on_error,
                                on_close=on_close)

    ws.run_forever()
