# backend services api endpoints specification

All endpoints are very simple and returns strings.

### auth-service

- /status [GET]:
    - response:
        - 200, 'OK'
- /test-services-conns [GET]:
    - response:
        - 200, 'OK'
        - 500, "connfail: list,of,not,responding,services"
- /authorize [POST]:
    - properties:
        - username [string]
        - password [string]
    - response:
        - 200, 'authorized'
        - 403, 'unauthorized'
        - 550, 'cannot connect to databases'

### content-generator

- /status [GET]:
    - response:
        - 200, 'OK'
- /test-services-conns [GET]:
    - response:
        - 200, 'OK'
        - 500, "connfail: list,of,not,responding,services"
- /generate-bs [GET]:
    - properties:
        - bs-type [int]
            - 1: img_name beautifier
    - response:
        - 200, <content-value>
        - 404, 'no-content-for-this-bs-type'
        - 550, 'cannot connect to databases'
        - 551, 'cannot connect to backend services'

### image-processor

- /status [GET]:
    - response:
        - 200, {'status': 'OK'}
- /test-services-conns [GET]:
    - response:
        - 200, {'status': 'OK'}
        - 500, {'connfail': 'list,of,not,responding,services'}
- /save-image [POST]:
    - properties:
        - image-name [string]
        - image-size [int]
    - response:
        - 200, {'status': 'image-saved'}
        - 570, {'status': 'image-not-saved'}
        - 550, {'status': 'cannot connect to databases'}
        - 551, {'status': 'cannot connect to backend services'}
- /replace-image [PUT]:
    - properties:
        - image-name [string]
        - image-size [int]
        - image-id [string]
    - response:
        - 200, {'status': 'image-replaced'}
        - 570, {'status': 'image-not-replaced'}
- /delete-image [DELETE]:
    - properties:
        - image-id [string]
    - response:
        - 200, {'status': 'image-deleted'}
        - 550, {'status': 'cannot connect to databases'}
        - 570, {'status': 'image-not-deleted'}

### mailing-service

- /status [GET]:
    - response:
        - 200, 'OK'
- /test-services-conns [GET]:
    - response:
        - 200, 'OK'
        - 500, "connfail: list,of,not,responding,services"
- /send-message [POST]:
    - properties:
        - author [string]
        - body [string]
        - addressee [string]
    - response:
        - 200, 'message-queued'
        - 570, 'could-not-enqueue-message'