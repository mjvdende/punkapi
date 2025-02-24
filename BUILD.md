# Building and testing Punk API

## Prerequisites
poetry
python

## Activate poetry shell
```shell
eval $(poetry env activate)  
```

## Run app
```shell
python punkapi/app.py
```

## Test
locally running tests the app is started autmatically

```shell
pytest
```

With coverage report generated

```shell
pytest --cov=punkapi --cov-report=html
```

## Performance test
```shell
locust --headless -u 5 -r 1 -t 30s --html locust_report.html
```
