# 🌐 Proxy Servers: Your Friendly Gateway on the Web

Proxy servers are essential intermediaries connecting clients and servers, enhancing security, performance, and privacy. They broadly fall into two categories:

- [**Forward Proxy**](#-what-is-a-forward-proxy)
- [**Reverse Proxy**](#-what-is-a-reverse-proxy)

Let’s dive into each one with detailed explanations

---

## 🔍 What is a Forward Proxy?

A **forward proxy** sits between a client and the internet. It forwards requests from clients to web servers and delivers responses back to the clients.

**Think of it as:** your helpful friend who fetches information from a library, keeping your identity secret.

### 🚦 How a Forward Proxy Works:

```
Client (requests a resource) --> Forward Proxy (fetches from the internet) --> Internet
Internet (sends response) --> Forward Proxy (returns response) --> Client
```

### 🛠️ Real-world Applications:
- **Privacy Protection**: Masks client IP addresses.
- **Access Control**: Filters and restricts website access based on content policies.
- **Resource Optimization**: Caches frequently accessed resources, reducing network traffic and improving load times.

### Example: Forward Proxy with Azure Virtual Machine

You can deploy a forward proxy using tools like Squid on an Azure Virtual Machine (VM). This setup secures and manages internet access for all resources within your Azure Virtual Network (VNet).

- **Step-by-step Approach:**
  - Deploy a Linux VM in Azure.
  - Install and configure Squid proxy server.
  - Set network security rules to allow access.

### 📌 Common Tools for Forward Proxy:
- **Squid**: Widely used for caching and internet traffic management.
- **Privoxy**: Known for advanced filtering capabilities and enhancing privacy.
- **Tinyproxy**: Lightweight and easy to configure.

### Example: Simple Forward Proxy
In the following Python code, the requests library is configured to use a forward proxy to make HTTP requests. The proxy dictionary defines the address of your forward proxy server. Requests sent through this proxy mask the client's IP address, providing anonymity.

```python
import requests

proxy = {
    'http': 'http://your_forward_proxy_ip:port',
    'https': 'http://your_forward_proxy_ip:port',
}

# Request routed via the forward proxy
response = requests.get('http://example.com', proxies=proxy)
print(response.text)
```

### 📌 VPN vs Forward Proxy
- **VPN (Virtual Private Network)**: Encrypts all traffic at the network level, providing full anonymity and security across all internet activities.
- **Forward Proxy**: Typically works at the application level, handling specific application requests without encrypting the entire network traffic.

---

## 🎯 What is a Reverse Proxy?

A **reverse proxy** sits between external clients (users) and internal servers. It handles client requests, forwards them to internal servers, and returns server responses back to the clients.

**Think of it as:** a receptionist directing visitors to the correct office inside a building.

### 🚦 How a Reverse Proxy Works:

```
Client (makes request) --> Reverse Proxy (forwards internally) --> Internal Server
Internal Server (responds) --> Reverse Proxy (returns response) --> Client
```

### 🛠️ Real-world Applications:
- **Load Balancing**: Distributes incoming traffic evenly across multiple servers.
- **Security Shield**: Conceals internal network architecture and protects servers from direct exposure.
- **SSL Management**: Manages SSL certificates and encrypts/decrypts traffic.
- **Caching**: Stores frequently accessed content to enhance speed and efficiency.

### Example: Reverse Proxy with Azure Application Gateway

Azure Application Gateway is a managed reverse proxy providing load balancing, security, and SSL termination.

- **Key Features:**
  - Automatic scaling to handle varying traffic.
  - SSL offloading and encryption.
  - URL-based routing to efficiently manage traffic.
  - Web Application Firewall (WAF) integration for enhanced security.

### 📌 Common Tools for Reverse Proxy:
- **Nginx**: Widely used for load balancing, SSL termination, caching, and URL rewriting.
- **HAProxy**: Known for high-performance load balancing and reliability.

### Example: Reverse Proxy Using FastAPI
The following FastAPI-based reverse proxy code receives client requests, forwards these requests to the backend server, and then sends the backend server's response back to the client. It transparently handles HTTP methods, headers, and body data.

```python
from fastapi import FastAPI, Request, Response
import requests

app = FastAPI()

BACKEND_SERVER = 'http://localhost:5001'

@app.api_route('/{path:path}', methods=['GET', 'POST', 'PUT', 'DELETE'])
async def proxy(path: str, request: Request):
    url = f"{BACKEND_SERVER}/{path}"
    method = request.method

    headers = dict(request.headers)
    body = await request.body()
    
    # Forward request to backend server
    resp = requests.request(method, url, headers=headers, data=body, params=request.query_params)

    # Return backend server's response to client
    return Response(content=resp.content, status_code=resp.status_code, headers=dict(resp.headers))

```

### 🖥️ Backend Server Example (FastAPI)
This simple FastAPI backend server returns a JSON response when accessed via the root endpoint.

```python
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def home():
    return {"message": "Hello from Backend Server!"}
```

Run the backend server using Uvicorn:

```
uvicorn backend_server:app --port 5001
```
