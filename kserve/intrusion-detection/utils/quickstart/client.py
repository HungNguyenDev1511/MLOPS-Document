import requests
import json

if __name__ == "__main__":
    # Define YOUR OWN authservice_session for authentication
    cookies = {
        "authservice_session": "MTY5OTk3MTkzNXxOd3dBTkRORFVWcFBSRVkyUlVaRlIxSXlSMGhGVUVsT1dFUk1XbFpGTWtGWlJUWlRORXRVUVVaUFJrUXlNMVZKUVVwRlRWTk1NMEU9fKd-yLOqo4UjVzu6KpGWV7IyM2lJPsNz5FliyqDEJBT-",
    }

    # We will send requests with content-type is json
    headers = {
        "Host": "sklearn-iris.kserve-test.example.com",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    # Define our data for prediction
    data = {
        "instances": [
            [6.8,  2.8,  4.8,  1.4],
            [6.0,  3.4,  4.5,  1.6]
        ]
    }

    # OR read this instead
    # with open('./iris-input.json') as f:
    #     data = f.read().replace('\n', '').replace('\r', '').encode()

    response = requests.post(
        "http://localhost:8000/v1/models/sklearn-iris:predict",
        cookies=cookies,
        data=json.dumps(data),
        headers=headers,
    )

    print(response)
