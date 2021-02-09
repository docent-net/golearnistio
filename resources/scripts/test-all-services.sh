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

function test_endpoint () {
    HTTP_METHOD=$1
    SCRIPT_PATH=$2
    FORM_DATA=$3

    TEST=$($CURL_CMD -X $HTTP_METHOD $FORM_DATA \
        ${ISTIO_SVC_image_processor}/$SCRIPT_PATH)
    if [[ $TEST != 200 ]]; then
        RETCODE=1
        echo "${ISTIO_SVC_image_processor}/${SCRIPT_PATH} : $TEST"
    fi
}

###################################################
# image-processor
###################################################

test_endpoint "GET" "status"
test_endpoint "GET" "test-services-conns"
test_endpoint "DELETE" "delete-image?image-id=abc"
test_endpoint "POST" "save-image" '-H "Content-Type: application/x-www-form-urlencoded" -d "image-name=test&image-size=1234"'
test_endpoint "PUT" "replace-image" '-H "Content-Type: application/x-www-form-urlencoded" -d "image-name=test1&image-size=6234&image-id-abd"'

# curl -s -o /dev/null -w "%{http_code}" -X POST -H "Content-Type: application/x-www-form-urlencoded" -d "image-name=test&image-size=1234" http://127.0.0.1:8001/save-image

###################################################
# content-generator
###################################################

###################################################
# mailing-service
###################################################

###################################################
# auth-service
###################################################
