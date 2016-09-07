import calendar
import time
import SimpleHTTPServer
import SocketServer

port = 8000


def get_time():
    return calendar.timegm(time.gmtime())


class TimeHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/time':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            current_time = "{{'time': {}}}".format(get_time())
            self.wfile.write(current_time)
        else:
            self.send_response(400)  # Bad Request

Handler = TimeHandler
http_server = SocketServer.TCPServer(("", port), Handler)
print "Starting HTTP Server on Port", port
http_server.serve_forever()
