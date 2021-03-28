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
# golearnistio: mailing-service
#
#   A dummy service pretending to manage sending emails
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


@app.route("/send-message", methods=['POST'])
@auth.login_required
def send_message_handler():
    """
    Send message dummy endpoint
    """

    author = request.data.get('msg-author', '', type=str)
    body = request.data.get('msg-body', '', type=str)
    addressee = request.data.get('msg-addressee', '', type=str)

    if not author or not body or not addressee:
        return {'status': 'incomplete-message-properties'}, 570

    # TODO: queue connections here - later, when queue work
    #   - 550, 'could-not-enqueue-message'
    # enqueue_message()

    # for now let's just pretend we do something
    sleep(0.15)

    return {'status': 'message-queued'}, status.HTTP_200_OK

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
    app.run(host="0.0.0.0", port=8004, debug=True)