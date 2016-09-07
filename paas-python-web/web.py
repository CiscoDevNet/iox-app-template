import SimpleHTTPServer
import SocketServer
port = 8000
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
http_server = SocketServer.TCPServer(("", port), Handler)
print "Starting HTTP Server on Port", port
http_server.serve_forever()
