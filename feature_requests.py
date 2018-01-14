from SimpleHTTPServer import SimpleHTTPRequestHandler
import SimpleHTTPServer, SocketServer, datetime, cgi, logging
from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from database import Base, FeatureRequests

# create session and connect to DB
engine = create_engine('sqlite:///featurerequests.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

class webServerHandler(SimpleHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        
    def do_GET(self):
        ''' Handles all Get Requests '''
        print "got get request %s" % (self.path)
        
        if self.path == '/':
            self.path = '/index.html'
            return SimpleHTTPRequestHandler.do_GET(self)
        if self.path == '/includes/styles.css':
            self.path = '/includes/styles.css'
            return SimpleHTTPRequestHandler.do_GET(self)
        if self.path == '/includes/f_requests.js':
            self.path = '/includes/f_requests.js'
            return SimpleHTTPRequestHandler.do_GET(self)
        
    
    def do_POST(self):
        ''' Handles all POST requests '''
        
        # new feature POST Request:
        if self.path.endswith("/feature/new"):
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD':'POST',
                         'CONTENT_TYPE':self.headers['Content-Type'],
                         })
            
            # retrieve data from form:
            form_title = form.getvalue('title')
            form_description = form.getvalue('description')
            form_client = form.getvalue('client')
            form_client_priority = form.getvalue('clientPriority')
            form_target_date = form.getvalue('targetDate')
            form_product_area = form.getvalue('productArea')
            
            # check to see if the priority exists in database for this client:
            records_found = session.query(FeatureRequests.feature_id).filter(FeatureRequests.client == form_client, FeatureRequests.client_priority == int(form_client_priority)).all()
            
            # if records_found contains data, then re-order the priorities before adding new record:
            if(len(records_found) > 0):
                # query records for client to get all priority levels:
                all_records_client = session.query(FeatureRequests.feature_id, FeatureRequests.client_priority).filter(FeatureRequests.client == form_client).all()
                
                target_priority = int(form_client_priority)
                
                status_finished = False
                
                while(status_finished == False):
                    # update existig records so that we can add the new record at the correct priority
                    try:
                        # find the index of target_priority record
                        index = [y[1] for y in all_records_client].index(target_priority)
                        
                        # update the record in the database:
                        update_obj = (session.query(FeatureRequests).filter(FeatureRequests.feature_id == all_records_client[index][0])).update({"client_priority": (FeatureRequests.client_priority + 1)})
                        
                        session.commit()
                        
                        # increment the target priority so that we can update the next record (if needed)
                        target_priority += 1
                    except ValueError:
                        # the target_priority isn't found in the list.
                        # Means, we are finished updating and can add the new record.
                        status_finished = True
                        
                        # add new record to database:
                        add_new_feature(form_title, form_description, form_client, form_client_priority, form_target_date, form_product_area)
            elif (len(records_found) == 0):
                # priority value is not taken, insert the new record into the database:
                add_new_feature(form_title, form_description, form_client, form_client_priority, form_target_date, form_product_area)
                
            self.send_response(201)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # write output to html page to let user know request was successfully submitted:
            self.wfile.write("<html><body>")
            self.wfile.write("<b>You have successfully submitted a new feature request.</b>")
            self.wfile.write("<p>To submit another request, click to return: <a href='/'>Return To Main Page</a></p>")
            self.wfile.write("</body></html>")
            
def add_new_feature(form_title, form_description, form_client, form_client_priority, form_target_date,  form_product_area):
    ''' Handles creating the new featureRequest object and inserting it into the database '''
    
    # create a new feature object and insert it into the database:
    new_feature = FeatureRequests(title=form_title,
                                  description = form_description,
                                  client=form_client,
                                  client_priority= int(form_client_priority),
                                  target_date=datetime.datetime.strptime(form_target_date, "%m/%d/%Y").date(),
                                  product_area = form_product_area)

    session.add(new_feature)
    session.commit()
    
def start_server():
    PORT = 8000
    
    httpd = SocketServer.TCPServer(("localhost", PORT), webServerHandler)
    
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