import requests
import json
from os import environ
import sys

# TODO: rewrite test-all-services.sh here

# verify whether svcs urls are set
SVCS_URLS={
    "image_processor": environ.get("ISTIO_SVC_image_processor"),
    "auth_service": environ.get("ISTIO_SVC_auth_service"),
    "content_generato": environ.get("ISTIO_SVC_content_generator"),
    "mailing_service": environ.get("ISTIO_SVC_mailing_service")
}
if None in SVCS_URLS.values():
    print("Looks like some SVCS urls are not set!")
    sys.exit()


def test_auth_svc_check_status_code_equals_200():
     response = requests.get(f'{SVCS_URLS["image_processor"]}/status')

     assert response.status_code == 200

def test_auth_svc_tests_svc_conn_code_equals_200():
     response = requests.get(f'{SVCS_URLS["image_processor"]}/test-services-conns')

     assert response.status_code == 200