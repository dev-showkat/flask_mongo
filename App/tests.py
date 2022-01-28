import unittest
from flask import json
import requests


class  TestHealthCheck(unittest.TestCase):
    def test_basic_route(self):
        response = requests.get('http://127.0.0.1:5000/');
        status = response.status_code
        self.assertEqual(status, 200)


class TestUsers(unittest.TestCase):
    def test_successful_signup(self):
        payload = json.dumps({
            "email": "a@gmail.com",
            "password": "pass"
        })
        response = requests.post('http://127.0.0.1:5000/users/signup', headers = {"Content-Type": "application/json"}, data = payload)
        self.assertEqual(response.status_code, 200)

    def test_successful_registration(self):
        response = requests.post('http://127.0.0.1:5000/users/registration', headers = {"Content-Type": "application/json", "token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFiY2RAZ21haWwuY29tIiwiaWQiOiI2MWYyNTNlNzQ1ZmRhM2RmOGMyMmY0NTUiLCJleHAiOjE2NDMzNjkzMjF9.z-Hi-oumM1JapaodNLqruZQcJmtmJA1GChIDwHfCjsk'})
        self.assertEqual(response.status_code, 201)

    def test_successful_users(self):
        response = requests.get('http://127.0.0.1:5000/users/')
        self.assertEqual(response.status_code, 200)

    def test_successful_user(self):
        response = requests.get('http://127.0.0.1:5000/users/61f2541c484663093f948d25');
        self.assertEqual(response.status_code, 200)

    def test_successful_login(self):
        payload = json.dumps({
            "email": "abcd@gmail.com",
            "password": "mycoolpassword"
        })
        response = requests.post('http://127.0.0.1:5000/users/login', headers = {"Content-Type": "application/json"}, data = payload);
        self.assertEqual(response.status_code, 200)

    def test_successful_deleted(self):
        payload = json.dumps({
            "email": "a@gmail.com",
            "password": "pass"
        })
        response = requests.delete('http://127.0.0.1:5000/users/61f2862b5459e908b25d6fb5', data = payload, headers =  {"Content-Type": "application/json", "token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFiY2RAZ21haWwuY29tIiwiaWQiOiI2MWYyNTNlNzQ1ZmRhM2RmOGMyMmY0NTUiLCJleHAiOjE2NDMzNjkzMjF9.z-Hi-oumM1JapaodNLqruZQcJmtmJA1GChIDwHfCjsk'});
        self.assertEqual(response.status_code, 204)

    def test_successful_forget_password(self):
        payload = json.dumps({
            "email": "shyxum96@gmail.com"
        })
        response = requests.post('http://127.0.0.1:5000/users/forget-password', headers = {"Content-Type": "application/json"}, data = payload);
        self.assertEqual(response.status_code, 200)

    def test_successful_reset_password(self):
        payload = json.dumps({
            "new_password": "shyxum96"
        })
        response = requests.put('http://127.0.0.1:5000/users/reset-password', headers = {"Content-Type": "application/json", 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InNoeXh1bTk2QGdtYWlsLmNvbSIsImV4cCI6MTY0MzI4OTk5OX0.KR-KGYUOPMS4Auv53BT7ZvAx3cjjPS8tcwrvXMRShAw' }, data = payload);
        self.assertEqual(response.status_code, 200)

    
class TestTodos(unittest.TestCase):
    def test_successful_create(self):
        payload = json.dumps({
            "title": "title",
            "description": "description"
        })
        response = requests.post('http://127.0.0.1:5000/todos/', headers = {"Content-Type": "application/json", "token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFiY2RAZ21haWwuY29tIiwiaWQiOiI2MWYyNTNlNzQ1ZmRhM2RmOGMyMmY0NTUiLCJleHAiOjE2NDMzNjkzMjF9.z-Hi-oumM1JapaodNLqruZQcJmtmJA1GChIDwHfCjsk'}, data = payload)
        self.assertEqual(response.status_code, 201)

    def test_successful_todos(self):
        response = requests.get('http://127.0.0.1:5000/todos/')
        self.assertEqual(response.status_code, 200)

    def test_successful_todo(self):
        response = requests.get('http://127.0.0.1:5000/todos/61f2a07d3ffa1213e78c7f95');
        self.assertEqual(response.status_code, 200)

    def test_successful_deleted(self):
        response = requests.delete('http://127.0.0.1:5000/todos/61f2a1b13ffa1213e78c7f9d', headers =  {"Content-Type": "application/json", "token": 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFiY2RAZ21haWwuY29tIiwiaWQiOiI2MWYyNTNlNzQ1ZmRhM2RmOGMyMmY0NTUiLCJleHAiOjE2NDMzNjkzMjF9.z-Hi-oumM1JapaodNLqruZQcJmtmJA1GChIDwHfCjsk'});
        self.assertEqual(response.status_code, 204)

    def test_successful_update(self):
        payload = json.dumps({
            "title": "new title",
        })
        response = requests.put('http://127.0.0.1:5000/todos/61f2a2c53ffa1213e78c7fa1', headers = {"Content-Type": "application/json", 'token': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6ImFiY2RAZ21haWwuY29tIiwiaWQiOiI2MWYyNTNlNzQ1ZmRhM2RmOGMyMmY0NTUiLCJleHAiOjE2NDMzNjkzMjF9.z-Hi-oumM1JapaodNLqruZQcJmtmJA1GChIDwHfCjsk' }, data = payload);
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
        