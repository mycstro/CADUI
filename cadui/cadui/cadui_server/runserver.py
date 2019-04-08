import http.server
import socketserver

PORT = 3333
Handler = http.server.SimpleHTTPRequestHandler

Server_Info = "Serving at port: {}".format(PORT),

with socketserver.TCPServer(("", PORT), Handler) as http:
    print(Server_Info)
    http.serve_forever()
