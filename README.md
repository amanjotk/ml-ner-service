# ml-ner-service

This is a very simple Named Entity Service using out of the box implementation
from spaCy library. 

The Flask app loads the spaCy model as a first step and receives POST requests with
JSON payloads and returns the entities in the input text with their corresponding entity type.

To run locally, you need to have Docker Desktop installed with Kubernetes enabled.

In order to run the Kubernetes cluster, run:

`kubectl apply -f deployment.yml`

followed by

`kubectl apply -f service.yml`

Check if the deployment is running 3 pods in a ready state by running `kubectl get pods`

Make POST requests to the service by hitting http://0.0.0.0/predict with a JSON payload with your text.