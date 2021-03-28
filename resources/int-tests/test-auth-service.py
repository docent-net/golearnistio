import config
import requests

# verify whether svcs urls are set
SVC_URL=config.read_svc_urls()["auth_service"]

def test_check_status_code_equals_200():
     response = requests.get(f'{SVC_URL}/status')

     assert response.status_code == 200

def test_tests_svc_conn_code_equals_200():
     response = requests.get(f'{SVC_URL}/test-services-conns')

     assert response.status_code == 200

def test_authorize_code_equals_200():
     data = {
          "username": "test_user",
          "password": "complexpassword"
     }
     response = requests.post(f'{SVC_URL}/authorize', data)

     assert response.status_code == 200

def test_authorize_code_equals_401():
     data = {
          "username": "incorrect_user",
          "password": "incorrect_password"
     }
     response = requests.post(f'{SVC_URL}/authorize', data)

     assert response.status_code == 401

def test_token_validation_equals_200():
    url=f'{SVC_URL}/verify-session-token?token={config.AUTH_TOKEN_CORRECT}'
    response = requests.get(url)

    assert response.status_code == 200

def test_token_validation_equals_401():
    url=f'{SVC_URL}/verify-session-token?token={config.AUTH_TOKEN_INCORRECT}'
    response = requests.get(url)

    assert response.status_code == 401