#!/bin/bash

###################################################
#
# This script iterates over all services endpoints
# and verifies whether any endpoint is failing
#
# Requirements:
#
# - Remember to run set-env-vars.sh to export URLs
#   of services
#
# Usage: ./test-all-services.sh
#
###################################################

CURL_CMD="curl -s -o /dev/null -w "%{http_code}

RETCODE=0

declare -A SVCS_URLS
SVCS_URLS[image_processor]=${ISTIO_SVC_image_processor}
SVCS_URLS[auth_service]=${ISTIO_SVC_auth_service}
SVCS_URLS[content_generator]=${ISTIO_SVC_content_generator}
SVCS_URLS[mailing_service]=${ISTIO_SVC_mailing_service}

function test_endpoint () {
    HTTP_URL=$1
    HTTP_METHOD=$2
    SCRIPT_PATH=$3
    FORM_DATA=$4
    echo "-> [$HTTP_METHOD] $HTTP_URL/$SCRIPT_PATH"

    TEST=$($CURL_CMD -X $HTTP_METHOD $FORM_DATA \
        $HTTP_URL/$SCRIPT_PATH)
    if [[ $TEST != 200 ]]; then
        RETCODE=1
        echo "${ISTIO_SVC_image_processor}/${SCRIPT_PATH} : $TEST"
    fi
}

###################################################
# image-processor
###################################################

echo -e "\n\nTesting ${SVCS_URLS[image_processor]}\n"
test_endpoint ${SVCS_URLS[image_processor]} "GET" "status"
test_endpoint ${SVCS_URLS[image_processor]} "GET" "test-services-conns"
test_endpoint ${SVCS_URLS[image_processor]} "DELETE" \
    "delete-image?image-id=abc"
test_endpoint ${SVCS_URLS[image_processor]} "POST" "save-image" \
    '-H "Content-Type: application/x-www-form-urlencoded" \
    -d image-name=test&image-size=1234'
test_endpoint ${SVCS_URLS[image_processor]} "PUT" "replace-image" \
    '-H "Content-Type: application/x-www-form-urlencoded" \
    -d image-name=test1&image-size=6234&image-id-abd'

# curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "image-name=test&image-size=1234" http://127.0.0.1:8001/save-image

###################################################
# mailing-service
###################################################

echo -e "\n\nTesting ${SVCS_URLS[mailing_service]}\n"
test_endpoint ${SVCS_URLS[mailing_service]} "GET" "status"
test_endpoint ${SVCS_URLS[mailing_service]} "GET" "test-services-conns"
test_endpoint ${SVCS_URLS[mailing_service]} "POST" "send-message" \
    '-H "Content-Type: application/x-www-form-urlencoded" \
    -d msg-author=test1&msg-body=qwerty&msg-addressee=ytr'


###################################################
# content-generator
###################################################

echo -e "\n\nTesting ${SVCS_URLS[content_generator]}\n"

###################################################
# auth-service
###################################################

echo -e "\n\nTesting ${SVCS_URLS[auth_service]}\n"
test_endpoint ${SVCS_URLS[auth_service]} "GET" "status"
test_endpoint ${SVCS_URLS[auth_service]} "GET" "test-services-conns"
test_endpoint ${SVCS_URLS[image_processor]} "POST" "authorize" \
    '-H "Content-Type: application/x-www-form-urlencoded" \
    -d username=test_user&password=complexpassword'