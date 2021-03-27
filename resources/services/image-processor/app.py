#!/usr/bin/env python
##########################################################################
#
#     (   )
#  (   ) (
#   ) _   )
#    ( \_
#  _(_\ \)__
# (____\___))
#
# BIG FAT WARNING:
#
# This is a shit code. Don't learn anything from it. It's supposed to work
# and be very easy to understand. Nothing more, nothing less.
#
# golearnistio: image-processor
#
#   A dummy service pretending to process uploaded images)
#
##########################################################################
from flask import request
from flask_api import FlaskAPI, status
from flask_httpauth import HTTPTokenAuth
import requests
import os
from time import sleep

app = FlaskAPI(__name__)
auth = HTTPTokenAuth()

@app.route("/", methods=['GET'])
@app.route("/status", methods=['GET'])
def status_handler():
    """
    Main endpoint + status
    """

    return {'status': 'OK'}, status.HTTP_200_OK

@auth.verify_token
def verify_token(token):
    AUTH_SERVICE_URL=os.environ['ISTIO_SVC_auth_service']

    try:
        req = requests.request(
            'GET',
            f'{AUTH_SERVICE_URL}/verify-session-token?token={token}',
            timeout=1
            )
    except (requests.exceptions.Timeout,
            requests.exceptions.ConnectionError) as e:
        return False
    except Exception:
        return False

    if req.status_code != 200 or req.json()['status'] != 'authorized':
        return False

    return req.json()['status']

@app.route("/delete-image", methods=['DELETE'])
@auth.login_required
def delete_image_handler():
    """
    Replace image dummy endpoint
    """

    img_id = request.args.get('image-id', '', type=str)

    if not img_id:
        return {'status': 'image-not-deleted'}, 570

    # TODO: DB connections here - later, when DB work
    #   - 550, 'cannot connect to databases'

    # for now let's just pretend we do something
    sleep(0.15)

    return {'status': 'image-deleted'}, status.HTTP_200_OK

@app.route("/replace-image", methods=['PUT'])
@auth.login_required
def replace_image_handler():
    """
    Replace image dummy endpoint
    """

    img_name = request.data.get('image-name', '', type=str)
    img_id   = request.data.get('image-id', '', type=str)
    img_size = request.data.get('image-size', '', type=int)

    if not img_name or not img_size or not img_id:
        return {'status': 'image-not-replaced'}, 570

    better_img_name = generate_better_img_name(img_name)
    if not better_img_name:
        return {'status': 'cannot connect to backend services'}, 551

    # TODO: queue connections here - later, when queue work
    #   - 550, 'cannot connect to queue'

    # for now let's just pretend we do something
    sleep(0.15)

    return {'status': 'image-replaced'}, status.HTTP_200_OK

@app.route("/save-image", methods=['POST'])
@auth.login_required
def save_image_handler():
    """
    Save image dummy endpoint
    """

    img_name = request.data.get('image-name', '', type=str)
    img_size = request.data.get('image-size', '', type=int)

    if not img_name or not img_size:
        return {'status': 'image-not-saved'}, 570

    better_img_name = generate_better_img_name(img_name)
    if not better_img_name:
        return {'status': 'cannot connect to backend services'}, 551

    #   - 551, 'cannot connect to backend services'
    # TODO: queue connections here - later, when queue work
    #   - 550, 'cannot connect to queue'
    # async_save_image_to_storage()
    # enqueue_image_processing()

    # for now let's just pretend we do something
    sleep(0.15)

    return {
        'status': f'image-saved:{better_img_name}'
        }, status.HTTP_200_OK

def generate_better_img_name(img_name):
    """
    Fetch improved image name from content generator
    """

    CONTENT_GENERATOR_URL=os.environ['ISTIO_SVC_content_generator']

    try:
        req = requests.request(
            'GET',
            f'{CONTENT_GENERATOR_URL}/generate-bs?bs-type=1',
            timeout=1
            )
    except (requests.exceptions.Timeout,
            requests.exceptions.ConnectionError) as e:
        return False
    except Exception:
        return False

    return req.json()['content']

@app.route("/test-services-conns", methods=['GET'])
def test_services_conns_handler():
    """
    Route returning status of connections between this service
    and rest of services
    """

    failed_services = []

    # todo: add verification of connection with queue

    for envvar_name, envvar_value in os.environ.items():
        if envvar_name.startswith('ISTIO_SVC_'):
            if not verify_service_connectivity(envvar_value):
                failed_services.append(envvar_name)

    if failed_services:
        return {'connfail': ','.join(failed_services)}, status.HTTP_500_INTERNAL_SERVER_ERROR

    return {'status': 'OK'}, status.HTTP_200_OK

def verify_service_connectivity(svc_url):
    """
    This method verifies whether connection to the URL provided in the URL
    works correctly
    """

    try:
        req = requests.request('GET', svc_url,timeout=1)
    except (requests.exceptions.Timeout,
            requests.exceptions.ConnectionError) as e:
        return False
    except Exception:
        pass

    if req.status_code == 200 and req.json()['status'] == 'OK':
        return True

    return False

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8001, debug=True)