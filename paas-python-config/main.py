# -*- coding: utf-8 -*-

# A basic example of using the IOx CAF Configuration File

import os
import json
import ConfigParser
import SimpleHTTPServer
import SocketServer

# Import a customized configuration values holder
import config_custom


class GetRequestHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    """
    Class for handling a request to the root path /
    """

    def do_GET(self):
        if self.path == '/':

            # Create the response
            response = {
                'billing_id': config_custom.billing_id,
                'customer_id' : config_custom.customer_id,
                'location_id' : config_custom.location_id,
            }

            # Optionally include other information
            if config_custom.is_note_displayed:
                response['note_text'] = config_custom.note_text

            # Write the response
            self.protocol_version = 'HTTP/1.1'
            self.send_response(200, 'OK')
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(bytes(json.dumps(response)))
            # self.path = '/'
            return

        # return SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET(self)


def main():
    """
    The main function
    :return:
    """

    # Load the deployed configuration file from the CAF_APP_CONFIG_FILE environment variable
    config_file = os.environ['CAF_APP_CONFIG_FILE']
    config = ConfigParser.SafeConfigParser()
    config.read(config_file)

    # Set our custom configuration variables for display
    config_custom.billing_id = config.getint("Customer", "billing_id")
    config_custom.customer_id = config.getint("Customer", "customer_id")
    config_custom.location_id = config.getint("Customer", "location_id")
    config_custom.is_note_displayed = config.getboolean("Note", "is_note_displayed")
    config_custom.note_text = config.get("Note", "note_text")

    # Start and serve the HTTP server
    ip_port = 8000
    server = SocketServer.TCPServer(('0.0.0.0', ip_port), GetRequestHandler)
    print "Starting HTTP Server on port", ip_port
    server.serve_forever()


if __name__ == '__main__':
    main()
