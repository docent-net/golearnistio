import config
import requests

# verify whether svcs urls are set
SVC_URL=config.read_svc_urls()["image_processor"]

def test_check_status_code_equals_200():
     response = requests.get(f'{SVC_URL}/status')

     assert response.status_code == 200

def test_tests_svc_conn_code_equals_200():
     response = requests.get(f'{SVC_URL}/test-services-conns')

     assert response.status_code == 200

def test_unauthorized_endpoints_return_401():
     endpoints = [
          {"e": "save-image", "m": "POST"},
          {"e": "replace-image", "m": "PUT"},
          {"e": "delete-image", "m": "DELETE"}
     ]

     for e in endpoints:
          url=f'{SVC_URL}/{e["e"]}'
          if e["m"] == "POST": response = requests.post(url)
          elif e["m"] == "DELETE": response = requests.delete(url)
          elif e["m"] == "PUT": response = requests.put(url)
          else: assert 1 == 0 # this shouldnt happen

          assert response.status_code == 401

def test_save_image_equals_200():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/save-image'
     data = {"image-name": "test.jpg", "image-size": 551000}
     response = requests.post(url, data, headers=headers)

     assert response.status_code == 200

def test_save_image_lacks_image_size_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/save-image'
     data = {"image-name": "test.jpg"}
     response = requests.post(url, data, headers=headers)

     assert response.status_code == 570

def test_save_image_lacks_image_name_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/save-image'
     data = {"image-size": 551000}
     response = requests.post(url, data, headers=headers)

     assert response.status_code == 570

def test_replace_image_equals_200():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/replace-image'
     data = {
          "image-name": "test.jpg",
          "image-size": 551000,
          "image-id": 123
     }
     response = requests.put(url, data, headers=headers)

     assert response.status_code == 200

def test_replace_image_lacks_image_size_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/replace-image'
     data = {"image-name": "test.jpg", "image-id": 123}
     response = requests.put(url, data, headers=headers)

     assert response.status_code == 570

def test_replace_image_lacks_image_id_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/replace-image'
     data = {"image-name": "test.jpg", "image-size": 551000}
     response = requests.put(url, data, headers=headers)

     assert response.status_code == 570

def test_replace_image_lacks_image_name_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/replace-image'
     data = {"image-id": 123, "image-size": 551000}
     response = requests.put(url, data, headers=headers)

     assert response.status_code == 570

def test_delete_image_equals_200():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/delete-image?image-id=123'
     response = requests.delete(url, headers=headers)

     assert response.status_code == 200

def test_delete_image_lacks_image_id_equals_570():
     t = config.AUTH_TOKEN_CORRECT
     headers = {"Authorization": f"Bearer {t}"}
     url=f'{SVC_URL}/delete-image'
     response = requests.delete(url, headers=headers)

     assert response.status_code == 570