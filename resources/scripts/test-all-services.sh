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
    TEST=$($CURL_CMD ${ISTIO_SVC_image_processor}/$1)
    if [[ $TEST != 200 ]]; then
        RETCODE=1
        echo "${ISTIO_SVC_image_processor}/$1 : $TEST"
    fi
}

###################################################
# image-processor
###################################################

test_endpoint "status"
test_endpoint "test-services-conns"

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
