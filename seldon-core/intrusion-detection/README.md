# How-to Guide
## Install Seldon System 
```shell
kubectl create namespace seldon-system

helm upgrade --install seldon-core seldon-core-operator \
    --version 1.15.1 \
    --repo https://storage.googleapis.com/seldon-charts \
    --set usageMetrics.enabled=true \
    --namespace seldon-system \
    --set istio.enabled=true
```
Create another namespace for all of our seldon deployments
```shell
kubectl create ns seldon
```

## Quick start

Deploy your first iris model using the following commands
```shell
kubectl apply -f deployments/quickstart.yaml
```

Port-forward to access the service locally via istio ingress
```shell
kubectl port-forward svc/istio-ingressgateway 8000:80 -n istio-system
```

Open Swagger UI at the following [address](http://localhost:8000/seldon/seldon/iris-model/api/v1.0/doc/) or [this](http://10.10.10.10:8080/seldon/seldon/iris-model/api/v1.0/doc/), and paste the following request body to enjoy the result.

```shell
{"data": {"ndarray": [[1,2,3,4]]}}
```

## Install Source2Image tool
Source2Image (s2i) is a tool which is used by Redhat to automatically create docker images from source code.

Install `s2i` following [this link](https://github.com/openshift/source-to-image#for-linux)

Build a custom image as follows. Please refer to [this documentation](https://docs.seldon.io/projects/seldon-core/en/v1.16.0/python/python_wrapping_s2i.html) if you want to understand more about this magic.

```shell
s2i build . seldonio/seldon-core-s2i-python3:1.17.1 fullstackdatascience/intrusion_detection:0.1
```

Feel free to replace `fullstackdatascience/intrusion_detection:0.1` by your own image.

Along with testing APIs by Swagger UI, you can use cURL similar to this. Please update your corresponding cookie.
```shell
curl 'http://localhost:8000/seldon/seldon/iris-model/api/v1.0/predictions' \
  -H 'Content-Type: application/json' \
  -H 'Cookie: authservice_session=MTY5OTIzMzE3NHxOd3dBTkZGS1ZsVlhTMGcyV2tOTlNEZERXVXRPVEVaSlZ6ZFNRa0ZKUWpaRVdrOVFSekpLUjBvelZFUlVNazlQV2xSRE0wUktVRkU9fECnA2G0l8e4Suv04Og8lnq1AqT113VuI23RFeq4wHmF' \
  --data-raw '{"data":{"ndarray":[[5.0, 0.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 255.0, 250.0, 0.98, 0.01, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]}}'
```

## Install KNative for outlier detection
Install Knative Eventing version 0.24.4. From version 0.25, it requires minimum version of Kubernetes is 1.20.

```shell
kubectl apply -f https://github.com/knative/eventing/releases/download/v0.24.4/eventing-crds.yaml
kubectl apply -f https://github.com/knative/eventing/releases/download/v0.24.4/eventing-core.yaml
```