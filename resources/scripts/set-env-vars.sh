#!/bin/bash

# set env vars w/test services URLs
export "ISTIO_SVC_image_processor"="http://127.0.0.1:8001"
export "ISTIO_SVC_auth_service"="http://127.0.0.1:8002"
export "ISTIO_SVC_content_generator"="http://127.0.0.1:8003"
export "ISTIO_SVC_mailing_service"="http://127.0.0.1:8004"