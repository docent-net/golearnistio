from os import environ
import sys

AUTH_TOKEN_CORRECT="correcttoken5"
AUTH_TOKEN_INCORRECT="incorrecttokena"

def read_svc_urls():
    SVCS_URLS={
        "image_processor": environ.get("ISTIO_SVC_image_processor"),
        "auth_service": environ.get("ISTIO_SVC_auth_service"),
        "content_generator": environ.get("ISTIO_SVC_content_generator"),
        "mailing_service": environ.get("ISTIO_SVC_mailing_service")
    }
    if None in SVCS_URLS.values():
        print("Looks like some SVCS urls are not set!")
        sys.exit()

    return SVCS_URLS