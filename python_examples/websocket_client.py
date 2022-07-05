import websocket
import _thread
import time
import rel
import json


def on_message(ws, message):
    print("Received:")
    print(message)


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

    ws.run_forever(dispatcher=rel)  # Set dispatcher to automatic reconnection
    rel.signal(2, rel.abort)  # Keyboard Interrupt

    print("RequestGetAll")
    ws.send("\"RequestGetAll\"")

    print("RequestGetTopicName")
    ws_req = {"RequestGetTopicName": {"topic_name": "SIFIS::Lights"}}
    ws.send(json.dumps(ws_req))

    print("RequestGetTopicUUID")
    ws_req = {"RequestGetTopicUUID": {"topic_name": "SIFIS::Lights", "topic_uuid": "FirstLight"}}
    ws.send(json.dumps(ws_req))

    print("RequestPubMessage")
    ws_req = {"RequestPubMessage": {"value": {"message": "hello"}}}
    ws.send(json.dumps(ws_req))

    print("RequestPostTopicUUID")
    ws_req = {
        "RequestPostTopicUUID": {
            "topic_name": "SIFIS:Shutters",
            "topic_uuid": "FirstShutter",
            "value": {
                "shutter_uuid": "FistShutter",
                "description": "First DHT Shutter",
                "connected": True
            }
        }
    }
    ws.send(json.dumps(ws_req))

    rel.dispatch()
