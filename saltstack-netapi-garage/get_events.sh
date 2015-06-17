#obsoleted by consumeWSevts.py

#!/bin/bash
token=$(curl -sSk http://localhost:8000/login -H 'Accept: application/x-yaml' -d username='saltuser' -d password='saltuser' -d eauth=pam | grep token | awk '{print $2}')
./python_ws.py $token $1
