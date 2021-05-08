import unittest
from app import app

class AppTests(unittest.TestCase):

    def test_landing_page_returns_200(self):

        #arrange
        client = app.test_client(self)
        
        #act
        response = client.get('/')
        statuscode = response.status_code
        print(response.content_type)

        #assert
        self.assertEqual(statuscode, 200)

    def test_landing_page_content_type_returns_html(self):

        #arrange
        client = app.test_client(self)

        #act
        response = client.get('/')
        content_type = response.content_type

        #assert
        self.assertEqual(content_type, 'text/html; charset=utf-8')
        
if __name__ == '__main__':
    
    unittest.main()