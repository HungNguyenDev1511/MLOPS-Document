import requests
import subprocess

NUM_REQUESTS = 10

if __name__ == '__main__':
    # Define YOUR OWN authservice_session for authentication
    cookies = {
        "authservice_session": "MTY5OTIzMzE3NHxOd3dBTkZGS1ZsVlhTMGcyV2tOTlNEZERXVXRPVEVaSlZ6ZFNRa0ZKUWpaRVdrOVFSekpLUjBvelZFUlVNazlQV2xSRE0wUktVRkU9fECnA2G0l8e4Suv04Og8lnq1AqT113VuI23RFeq4wHmF",
    }

    # We will send requests with content-type is json
    headers = {
        "Content-Type": "application/json",
    }

    # Define our data for prediction
    json_data = {
        "data": {
            "ndarray": [[5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 255.0, 250.0, 0.98, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]],
        },
    }

    # Continuously send requests to the server
    for i in range(NUM_REQUESTS):
        response = requests.post(
            "http://localhost:8000/seldon/seldon/intrusion/api/v1.0/predictions",
            cookies=cookies,
            headers=headers,
            json=json_data,
        )

    # Retrieve all logs
    main_count = subprocess.check_output(
        "kubectl logs $(kubectl get pod -lseldon-app=intrusion-main -o jsonpath='{.items[0].metadata.name}') detector | grep \"AnomalyDetectionModel:predict\" | wc -l", 
        shell=True,
        )
    print(f"Number of requests to main: {int(main_count)}")
    canary_count = subprocess.check_output(
        "kubectl logs $(kubectl get pod -lseldon-app=intrusion-canary -o jsonpath='{.items[0].metadata.name}') detector | grep \"AnomalyDetectionModel:predict\" | wc -l", 
        shell=True,
        )
    print(f"Number of requests to main: {int(canary_count)}")
