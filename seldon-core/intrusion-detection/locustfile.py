from locust import HttpUser, task

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

class ModelUser(HttpUser):
    @task
    def detect(self):
        seldon_deplopyment_name = "seldon-model-autoscale"
        self.client.post(
            f"/seldon/seldon/{seldon_deplopyment_name}/api/v1.0/predictions",
            cookies=cookies,
            headers=headers,
            json=json_data,
        )