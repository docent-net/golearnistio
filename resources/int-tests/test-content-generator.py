import config
import requests

# verify whether svcs urls are set
SVC_URL=config.read_svc_urls()["content_generator"]

def test_check_status_code_equals_200():
     response = requests.get(f'{SVC_URL}/status')

     assert response.status_code == 200

def test_tests_svc_conn_code_equals_200():
     response = requests.get(f'{SVC_URL}/test-services-conns')

     assert response.status_code == 200

def test_unauthorized_generate_bs_equals_401():
     url=f'{SVC_URL}/generate-bs?bs-type=1'
     response = requests.post(url)

     assert response.status_code == 401

def test_generate_bs_equals_200_and_returns_content():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/generate-bs?bs-type=1'
     response = requests.get(url, headers=headers)

     assert response.status_code == 200

     assert isinstance(response.json()["content"], str)

def test_generate_bs_equals_404_for_nonexistant_type():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/generate-bs?bs-type=666'
     response = requests.get(url, headers=headers)

     assert response.status_code == 404