# Quadratic Equation Function

### To build image:
```shell
docker build -t pwc-quadratic:latest .
```

### To run container:
```shell
docker run -p 5000:5000 pwc-quadratic
```

### Endpoint with example parameters:

http://localhost:5000/print-plot?a=1&b=0&c=0&x_min=-5&x_max=5&y_min=0&y_max=10