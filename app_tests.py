import unittest
from unittest.mock import patch
from app import app, collection
from flask import session

class PagesTests(unittest.TestCase):

    def test_landing_page_returns_200(self):

        #arrange
        client = app.test_client(self)
        
        #act
        response = client.get('/')
        statuscode = response.status_code

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

    def test_signup_page_returns_200(self):

        #arrange
        client = app.test_client(self)

        #act
        response = client.get('/signup')
        content_type = response.status_code

        #assert
        self.assertEqual(content_type, 200)

    def test_user_page_returns_400_when_not_logged_in(self):

        #arrange
        client = app.test_client(self)

        #act
        response = client.get('/user')
        status_code = response.status_code

        #assert
        self.assertEqual(status_code, 400)

class DatabaseTests(unittest.TestCase):

    def test_creating_account_returns_200(self):

        client = app.test_client(self)

        response = client.post(
            '/signup',
            data = dict(
                name="bobpatel",
                username="tester12345", #unique username
                password="IloveShopify;)",  #passwords match
                confirm_pass='IloveShopify;)'
            ),
            follow_redirects=True
        )

        status_code = response.status_code

        self.assertTrue(status_code, 200)

    def test_passwords_dont_match_returns_400(self):

        client = app.test_client(self)

        response = client.post(
            '/signup',
            data = dict(
                name="bobpatel",
                username="temptester10", #unique username
                password="IloveShopify;)",  #different passwords
                confirm_pass='differentpassword'
            ),
            follow_redirects=True
        )

        status_code = response.status_code
        
        self.assertTrue(status_code, 400)

        collection.delete_one({'username': 'temptester10'})

    def test_username_already_exists_returns_400(self):

        client = app.test_client(self)

        collection.insert_one({'username': 'temptester10'})

        response = client.post(
            '/signup',
            data = dict(
                name="bobpatel",
                username="temptester10", #same username the username added on line 104
                password="IloveShopify;)",
                confirm_pass='IloveShopify;)' #same passwords
            ),
            follow_redirects=True
        )

        status_code = response.status_code
        
        self.assertTrue(status_code, 400)

        collection.delete_one({'username': 'temptester10'})

    def test_incorrect_password_returns_400(self):

        client = app.test_client(self)

        response = client.post(
            '/check',
            data = dict(
                username="tester12345",
                password="incorrectpassword"
            )
        )

        status_code = response.status_code

        self.assertTrue(status_code, 400)

    def test_username_doesnt_exist_returns_400(self):

        client = app.test_client(self)

        response = client.post(
            '/check',
            data = dict(
                username="username_that_is_not_in_database",
                password="randompassword12"
            )
        )

        status_code = response.status_code

        self.assertTrue(status_code, 400)

    def test_user_login_returns_200(self):

        client = app.test_client(self)

        response = client.post(
            '/check',
            data = dict(
                username="tester12345",
                password="IloveShopify;)"
            ),
            follow_redirects=True
        )

        status_code = response.status_code

        self.assertTrue(status_code, 200)

if __name__ == '__main__':
    
    unittest.main()