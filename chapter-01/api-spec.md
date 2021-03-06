# backend services api endpoints specification

All endpoints are very simple and returns strings.

### auth-service

- /status [GET]:
    - response:
        - 200, {'status': 'OK'}
- /test-services-conns [GET]:
    - response:
        - 200, {'status': 'OK', 'session-token': '<some-md5-string:32>'}
        - 500, {'connfail': 'list,of,not,responding,services'}
- /authorize [POST]:
    - properties:
        - username [string]
        - password [string]
    - response:
        - 200, {'status': 'authorized'}
        - 403, {'status': 'unauthorized'}
- /verify-session-token [GET]:
    - properties:
        - token [string]
    - response:
        - 200, {'status': 'authorized'}
        - 403, {'status': 'unauthorized'}

### content-generator

- /status [GET]:
    - response:
        - 200, {'status': 'OK'}
- /test-services-conns [GET]:
    - response:
        - 200, {'status': 'OK'}
        - 500, {'connfail': 'list,of,not,responding,services'}
- [auth required]: /generate-bs [GET]:
    - properties:
        - bs-type [int]
            - 1: img_name beautifier
    - response:
        - 200, {'content': '<some content>'}
        - 404, {'status': 'no-content-for-this-bs-type'}

### image-processor

- /status [GET]:
    - response:
        - 200, {'status': 'OK'}
- /test-services-conns [GET]:
    - response:
        - 200, {'status': 'OK'}
        - 500, {'connfail': 'list,of,not,responding,services'}
- [auth required]: /save-image [POST]:
    - properties:
        - image-name [string]
        - image-size [int]
    - response:
        - 200, {'status': 'image-saved'}
        - 570, {'status': 'image-not-saved'}
        - 550, {'status': 'cannot connect to queue'}
        - 551, {'status': 'cannot connect to backend services'}
- [auth required]: /replace-image [PUT]:
    - properties:
        - image-name [string]
        - image-size [int]
        - image-id [string]
    - response:
        - 200, {'status': 'image-replaced'}
        - 570, {'status': 'image-not-replaced'}
- [auth required]: /delete-image [DELETE]:
    - properties:
        - image-id [string]
    - response:
        - 200, {'status': 'image-deleted'}
        - 550, {'status': 'cannot connect to queue'}
        - 570, {'status': 'image-not-deleted'}

### mailing-service

- /status [GET]:
    - response:
        - 200, {'status': 'OK'}
- /test-services-conns [GET]:
    - response:
        - 200, {'status': 'OK'}
        - 500, {'connfail': 'list,of,not,responding,services'}- /send-message [POST]:
- [auth required]: /send-message [POST]:
    - properties:
        - msg-author [string]
        - msg-body [string]
        - msg-addressee [string]
    - response:
        - 200, {'status': 'message-queued'}
        - 570, {'status': 'incomplete-message-properties'}
        - 571, {'status': 'could-not-enqueue-message'}