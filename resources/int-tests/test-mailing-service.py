import config
import requests

# verify whether svcs urls are set
SVC_URL=config.read_svc_urls()["mailing_service"]

def test_check_status_code_equals_200():
     response = requests.get(f'{SVC_URL}/status')

     assert response.status_code == 200

def test_tests_svc_conn_code_equals_200():
     response = requests.get(f'{SVC_URL}/test-services-conns')

     assert response.status_code == 200

def test_unauthorized_send_message_equals_401():
     url=f'{SVC_URL}/send-message'
     response = requests.post(url)

     assert response.status_code == 401

def test_send_message_equals_200():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/send-message'
     data = {
          "msg-author": "Arsin Lupine",
          "msg-body": "message body",
          "msg-addressee": "arsin.lupine@domain.com"
     }
     response = requests.post(url, data, headers=headers)

     assert response.status_code == 200

def test_send_message_lacks_msg_author_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/send-message'
     data = {
          "msg-body": "message body",
          "msg-addressee": "arsin.lupine@domain.com"
     }
     response = requests.post(url, data, headers=headers)

     assert response.status_code == 570

def test_send_message_lacks_msg_body_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/send-message'
     data = {
          "msg-author": "Arsin Lupine",
          "msg-addressee": "arsin.lupine@domain.com"
     }
     response = requests.post(url, data, headers=headers)

     assert response.status_code == 570

def test_send_message_lacks_msg_addressee_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/send-message'
     data = {
          "msg-body": "message body",
          "msg-addressee": "arsin.lupine@domain.com"
     }
     response = requests.post(url, data, headers=headers)

     assert response.status_code == 570