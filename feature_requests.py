import SimpleHTTPServer
import SocketServer
import threading

def start_server():
    PORT = 8000
    
    Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
    
    httpd = SocketServer.TCPServer(("localhost", PORT), Handler)
    
    print "serving at port", PORT
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print ("Quitting")
        httpd.socket.close()
    
def main():
    start_server()
    
if __name__ == '__main__':
    main() 