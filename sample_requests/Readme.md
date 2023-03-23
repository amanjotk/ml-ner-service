## Command for load testing with Hey

`hey -z 5m -c 10 -m POST -H "Content-Type: application/json" -D sample_requests/request.json http://0.0.0.0:80/predict`