import calendar
import time
import SimpleHTTPServer
import SocketServer
import paho.mqtt.client as mqtt

port = 8000


def get_time():
    return calendar.timegm(time.gmtime())

def send_message():
    client = mqtt.Client()
    client.connect("iot.eclipse.org", 1883, 60)

    message = mqtt.MQTTMessage()
    message.payload = "Something Interesting Happened"

    client.publish("iox/test", message)
    client.disconnect()

#     # Blocking call that processes network traffic, dispatches callbacks and
#     # handles reconnecting.
#     # Other loop*() functions are available that give a threaded interface and a
#     # manual interface.
#     client.loop_forever()

class MQTTHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/mqtt':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            current_time = "{{'time': {}}}".format(get_time())
            self.wfile.write(current_time)
        else:
            self.send_response(400)  # Bad Request

Handler = MQTTHandler
http_server = SocketServer.TCPServer(("", port), Handler)
print "Starting HTTP Server on Port", port
http_server.serve_forever()
