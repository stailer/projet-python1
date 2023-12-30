#!/bin/bash

python3 -m debugpy --listen 0.0.0.0:5679 --wait-for-client -m flask run -h 0.0.0.0 -p 5000 --reload --cert=adhoc 