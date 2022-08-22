import prometheus_client
import time

# Create a metric to track time spent and requests made.
REQUEST_TIME = prometheus_client.Summary('request_processing_seconds', 'Time spent processing request')


# Decorate function with metric.
@REQUEST_TIME.time()
def process_request(t):
    """A dummy function that takes some time."""
    time.sleep(t)


def counter():
    c = prometheus_client.Counter('my_requests_total', 'HTTP Failures', ['method', 'endpoint'])
    c.labels('get', '/').inc(1)
    c.labels('post', '/submit').inc(1)


def latency():
    s = prometheus_client.Summary('request_latency_seconds', 'Description of summary')
    s.observe(4.7)    # Observe 4.7 (seconds in this case)

# if __name__ == '__main__':
#     # Start up the server to expose the metrics.
#     start_http_server(8000)
#     # Generate some requests.
#     while True:
#         process_request(random.random())