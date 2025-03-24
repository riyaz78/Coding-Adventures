import requests

proxy = {
    'http': 'http://your_forward_proxy_ip:port',
    'https': 'http://your_forward_proxy_ip:port',
}

response = requests.get('http://example.com', proxies=proxy)
print(response.text)