from nose.tools import assert_true
import urllib2
import requests

from feature_requests import webServerHandler

mock_server_port = 8000

def test_request_response():
    url = 'http://localhost:{port}/'.format(port=mock_server_port)

    # Send a request to the mock API server and store the response.
    response = requests.get(url)

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)

def test_view_all_request_response():
    url = 'http://localhost:{port}/view_all.html'.format(port=mock_server_port)
    
    response = requests.get(url)

    # Confirm that the request-response cycle completed successfully.
    assert_true(response.ok)
    
def test_view_all_client_data_retrieved():
    url = 'http://localhost:{port}/view_all.html'.format(port=mock_server_port)
    
    response=urllib2.urlopen(url)
    
    # read response 
    html=response.read()
    
    # check html to see if the client headers are found
    assert_true("Client A" in html)
    assert_true("Client B" in html)
    assert_true("Client C" in html)
  

    