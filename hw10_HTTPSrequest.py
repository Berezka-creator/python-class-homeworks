import http.server


# Create the content that will be sent when handling an HTTP request
class Handler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        # Send an 'OK' status back
        self.send_response(200)
        #Create data with the content type as HTML
        self.send_header('Content-Type', 'text-html')
        self.end_headers()
        #Write what will be displayed on the web page
        self.wfile.write('<h1>Hello</h1><p>This is a memorable text</p>'.encode())

# If we are running this file as the main, then lets create the server
if __name__ == '__main__':
    server = ('', 8118)
    httpd = http.server.HTTPServer(server, Handler)
    #handle the request just once (NOT forever)
    httpd.handle_request()
