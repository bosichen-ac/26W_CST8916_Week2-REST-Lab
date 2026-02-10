# Week 2 REST Lab

This project demonstrates a simple REST API built with Python's Flask framework. The API performs CRUD (Create, Read, Update, Delete) operations on user data, which can be tested locally and deployed to Azure App Service for cloud hosting.

---

## Part 1: HTTP Fundamentals

Before building APIs, it's important to understand how HTTP requests and responses work. This section introduces two tools for sending HTTP requests:
- **curl** (command line)
- **REST Client** extension in **Visual Studio Code**

### What is curl?
- **curl** is a command-line tool for making network requests.
- It supports many protocols (HTTP, HTTPS, FTP, etc.), but we'll use it mainly for **HTTP APIs**.
- It's fast, lightweight, and available on almost all systems.
- Perfect for practicing and automating API requests directly from the terminal.

**Example:**
```bash
curl https://jsonplaceholder.typicode.com/posts/1
```
This fetches data for the post with `ID` `1` and prints it in the terminal.

### What is the REST Client (VS Code Extension)?
- A Visual Studio Code extension that lets you send HTTP requests right from your editor.
- Requests are written in plain text files (.http), making them easy to save, share, and reuse.
- Responses show up in a side panel in VS Code, with support for JSON formatting and syntax highlighting.
- Great for who prefer a GUI-like experience inside VS Code rather than the terminal.

### How Requests and Responses Work
```
+-----------+         HTTP Request          +-------------------+
|           |  ------------------------->   |                   |
|   Client  |                               |       Server      |
| (curl or  |   <-------------------------  | (JSONPlaceholder) |
| REST API) |         HTTP Response         |                   |
+-----------+                               +-------------------+

```

### Prerequisites for curl

#### Ubuntu / Linux
- `curl` is usually pre-installed. If not:
  ```bash
  sudo apt update
  sudo apt install curl -y
  ```
- Inside VS Code, install the **REST Client** extension from the Extensions Marketplace.

#### Windows
- If you are using **Windows 10 or later**, `curl` is already included.
- Check with:
  ```powershell
  curl --version
  ```
- Open VS Code → Extensions → Search for **REST Client** → Install.

#### macOS
- `curl` is pre-installed.
- To confirm:
  ```bash
  curl --version
  ```
- Install the **REST Client** extension in VS Code.

---

### Activity: Sending HTTP Requests with curl

#### Step 1: Basic GET Request
```bash
curl https://jsonplaceholder.typicode.com/posts/1
```

#### Step 2: Show Headers with Response
```bash
curl -i https://jsonplaceholder.typicode.com/posts/1
```

#### Step 3: Send a POST Request (Create Resource)
```bash
curl -X POST https://jsonplaceholder.typicode.com/posts -H "Content-Type: application/json" -d '{"title":"My First Post","body":"Hello REST!","userId":1}'
```

#### Step 4: Send a DELETE Request
```bash
curl -X DELETE https://jsonplaceholder.typicode.com/posts/1
```

---

### When to Use curl, REST Client, or Code?

Each tool has its own strengths. Here's a quick guide:

| Tool                      | Best For                                 | Pros                                                          | Cons                                      |
| ------------------------- | ---------------------------------------- | ------------------------------------------------------------- | ----------------------------------------- |
| **curl**                  | Quick testing in the terminal            | Fast, works everywhere, good for automation in shell scripts  | Harder to read/write for complex requests |
| **REST Client**           | Learning & manual testing inside VS Code | Easy to use, readable request files, nice formatted responses | Only works inside VS Code                 |
| **Code (Python/JS/etc.)** | Building real applications               | Can reuse data in programs, automate workflows, connect APIs  | Requires coding knowledge, more setup     |

Think of it like this:
- **curl** → Quick, command-line experiments
- **REST Client** → Beginner-friendly exploration inside VS Code
- **Programming** → Real apps where your code actually *uses* the data

---

## Part 2: Flask REST API Demo

## Features

- Welcome message at root URL
- Health check endpoint
- Retrieve all users
- Retrieve a specific user by ID
- Create a new user
- Update an existing user
- Delete a user

## Prerequisites

Before you can run or deploy this app, you need to have the following installed:

- Python 3.x
- pip (Python package manager)
- Flask (`pip install Flask`)
- gunicorn (`pip install gunicorn`)
- Azure CLI (optional, for deployment)

## Project Structure

- app.py: Main Flask application
- requirements.txt: List of Python dependencies
- test-api.http: Test the REST API using the REST Client extension in Visual Studio Code
- client.html: Browser-based client to interact with the API (Part 3)
- README.md: Documentation

## Running Locally

To run the Flask API on your local machine:

1. **Fork this repository** by clicking the "Fork" button at the top right of the GitHub page. This creates your own copy of the repository under your GitHub account.

2. **Clone your forked repository** (replace `YOUR-USERNAME` with your GitHub username):

   ```bash
   git clone https://github.com/YOUR-USERNAME/26W_CST8916_Week2-REST-Lab.git
   ```

3. Navigate to the project directory:
   ```bash
   cd 26W_CST8916_Week2-REST-Lab
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:
   ```bash
   python app.py
   ```

6. The API will be running at http://127.0.0.1:8000

7. Use **test-api.http** to test the REST API using the REST Client extension in Visual Studio Code.

## Deploying to Azure

### What is Azure App Service?

[Azure App Service](https://learn.microsoft.com/en-us/azure/app-service/) is a fully managed platform for building, deploying, and scaling web apps. With Azure App Service, you can host web applications, REST APIs, and mobile backends in any programming language without managing infrastructure. It provides integrated continuous deployment and scaling features, making it a powerful and flexible solution for cloud-based web hosting.

Some key features of Azure App Service include:
- **Automatic Scaling**: Scale up or out depending on traffic.
- **Continuous Integration/Continuous Deployment (CI/CD)**: Easily integrate with GitHub, Bitbucket, or Azure DevOps for automated deployments.
- **Custom Domains and SSL**: Secure your apps with custom domains and certificates.
- **Load Balancing**: Built-in load balancing to handle high-traffic applications.
- **Monitoring and Diagnostics**: Access real-time monitoring and logs for troubleshooting.


You can learn more about Azure App Service and its features in the [official documentation](https://learn.microsoft.com/en-us/azure/app-service/).

To learn how to deploy a Python web app (Django, Flask, or FastAPI) to Azure App Service, refer to the [Quickstart Guide](https://learn.microsoft.com/en-us/azure/app-service/quickstart-python?tabs=flask%2Cwindows%2Cazure-cli%2Cazure-cli-deploy%2Cdeploy-instructions-azportal%2Cterminal-bash%2Cdeploy-instructions-zip-azcli). This guide walks you through deploying a Python web app to Azure, leveraging App Service to run your app in a Linux server environment.

## Why the URL is different (Local vs Azure)

When you run your Flask API **on your own laptop**:
- Flask is started with `python app.py`.
- You tell it to listen on **port 8000**.
- The URL is:  
  **http://localhost:8000/**  
  - **localhost** = your own computer  
  - **8000** = the port number you picked  

When you deploy the same app to **Azure App Service**:
- Azure gives your app a **public web address** like:  
  **https://cst8916-ramy-xxxx.azurewebsites.net/**
- Azure always serves your site using the **standard web ports**:  
  - **80** for HTTP  
  - **443** for HTTPS (secure)  
- That’s why the browser only shows `https://...` — because port 443 is the default.


### Think of it like this
- **Localhost:8000** → your house, back door, you choose the number (“8000”).  
- **Azure URL (443)** → a public library with one main entrance, number already set (443 = HTTPS).  
  You can’t change the public entrance — Azure manages it.


### Diagram

```text
LOCAL (your laptop)                          AZURE (cloud hosting)
───────────────────────                      ─────────────────────────────
Browser → http://localhost:8000/             Browser → https://yourapp.azurewebsites.net/
          |                                             |
          | port 8000 (you chose it)                    | port 443 (default HTTPS)
          ↓                                             ↓
      Flask app (python app.py)                   Azure front door → your Flask app
                                                  (internally still listening 8000)
```

## High-Level ASCII diagram

```
┌──────────────────────────────────────────────────────────────────────────────┐
│                         Flask REST API — Big Picture                         │
├──────────────────────────────────────────────────────────────────────────────┤
│ Clients                                                                      │
│ ┌────────────────────────┐     HTTP (JSON)     ┌───────────────────────────┐ │
│ │ VS Code REST Client    │  ─────────────────► │  Flask App (app.py)       │ │
│ │ (test-api.http)        │ ◄─────────────────  │  run: python app.py       │ │
│ └────────────────────────┘                     │  port: 8000               │ │
│ ┌────────────────────────┐                     │                           │ │
│ │ Browser / curl /Postman│                     │ Routes /  Endpoints       │ │
│ └────────────────────────┘                     │  ───────────────────────  │ │
│                                                │  GET    /                 │ │
│                                                │  GET    /health           │ │
│                                                │  GET    /users            │ │
│                                                │  GET    /users/{id}       │ │
│                                                │  POST   /users            │ │
│                                                │  PUT    /users/{id}       │ │
│                                                │  DELETE /users/{id}       │ │
│                                                └─────────────┬─────────────┘ │
│                                                              │               │
│                                                              ▼               │
│                                                ┌───────────────────────────┐ │
│                                                │ In-Memory User Store      │ │
│                                                │ (e.g., list/dict)         │ │
│                                                │                           │ │
│                                                └───────────────────────────┘ │
│                                                                              │
├──────────────────────────────────────────────────────────────────────────────┤
│ Local Dev Flow                                                               │
│    git clone → cd project → pip install -r requirements.txt → python app.py  │
│    → Test with test-api.http or browser → iterate                            │
├──────────────────────────────────────────────────────────────────────────────┤
│ Deploy to Azure App Service (Linux)                                          │
│                                                                              │
│ ┌───────────────┐     push / az deploy      ┌──────────────────────────────┐ │
│ │ GitHub Repo   │ ────────────────────────► │ Azure App Service (Gunicorn) │ │
│ └───────────────┘                           │ Public URL (HTTPS)           │ │
│                                             │ Auto scale • Logging • CI/CD │ │
│                                             └──────────────────────────────┘ │
├──────────────────────────────────────────────────────────────────────────────┤
│ Project Structure (key files)                                                │
│   app.py          → Flask application & routes                               │
│   requirements.txt → Python dependencies                                     │
│   test-api.http    → Ready-made requests for REST Client                     │
│   README.md        → Documentation                                           │
└──────────────────────────────────────────────────────────────────────────────┘
```

---

## Part 3: HTML/JavaScript Client

This section introduces a browser-based client that consumes the Flask REST API using JavaScript's `fetch()` API. This completes the full picture: you see both sides of REST communication, the server (Flask) and the client (browser).

### What is the fetch() API?

`fetch()` is JavaScript's built-in way to make HTTP requests, it's like `curl`, but for web browsers.

Think of it this way:
| Tool      | Where it runs        | Example                                |
| --------- | -------------------- | -------------------------------------- |
| `curl`    | Terminal             | `curl http://localhost:8000/users`     |
| `fetch()` | Browser (JavaScript) | `fetch('http://localhost:8000/users')` |

Both do the same thing: send an HTTP request and get a response.

**Example — GET all users:**
```javascript
// Send a GET request to the API
fetch('http://localhost:8000/users')
    .then(response => response.json())  // Convert response to JSON
    .then(data => console.log(data));   // Do something with the data
```

**Example — POST a new user:**
```javascript
// Send a POST request with data
fetch('http://localhost:8000/users', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ name: 'Charlie', age: 28 })
})
    .then(response => response.json())
    .then(data => console.log(data));
```

The `.then()` parts handle the response when it arrives (since network requests take time).

### What is CORS?

**CORS (Cross-Origin Resource Sharing)** is a browser security feature that prevents websites from making requests to other websites without permission.

By default, web browsers are paranoid. They block websites from talking to each other to keep you safe. CORS is the specific mechanism that allows them to talk safely.

![CORS Explained](cors-explained.png)

*Left: Without CORS, the browser (security guard) blocks your website from accessing another server. Right: With CORS enabled, the server says "this website is on my allowed list" and the browser lets the request through.*

**Why does this matter?**

Imagine you open `client.html` on your computer. The browser sees two different "addresses":
- The HTML file: `file:///C:/projects/client.html` (your computer)
- The API: `http://localhost:8000` (the Flask server)

These are **different origins** (different addresses). By default, browsers block this for security reasons — they don't want random websites stealing data from other sites.

**The problem:**
```
Browser: "Hey API, give me the users list"
API: "Here you go!"
Browser: "Wait... you're from a different origin. BLOCKED!"
```

**The solution:**

The API needs to say "It's okay, I allow requests from other origins." We do this by adding `flask-cors` to our Flask app:

```python
from flask_cors import CORS
CORS(app)  # Tell browsers: "Allow requests from anywhere"
```

Now the browser allows the request because the API explicitly permits it.

### Running the Client

#### Local Development

1. Make sure the Flask API is running:
   ```bash
   python app.py
   ```

2. Open `client.html` in your browser:
   - Double-click the file, OR
   - Use VS Code's Live Server extension, OR
   - Open directly: `file:///path/to/client.html`

3. The API URL should be `http://localhost:8000` (default)

4. Click **"Check Health"** to verify the connection, then **"Refresh Users"** to load data

#### With Azure Deployment

1. Deploy your Flask API to Azure App Service (see Part 2)

2. Open `client.html` in your browser

3. Change the API Base URL to your Azure URL:
   ```
   https://<your-app-name>.azurewebsites.net
   ```

4. Click **"Check Health"** to verify the connection

### Client Features

| Feature      | HTTP Method | Endpoint      | Description                  |
| ------------ | ----------- | ------------- | ---------------------------- |
| Health Check | GET         | `/health`     | Verify API is running        |
| List Users   | GET         | `/users`      | Display all users in a table |
| Create User  | POST        | `/users`      | Add a new user via form      |
| Edit User    | PUT         | `/users/<id>` | Update existing user         |
| Delete User  | DELETE      | `/users/<id>` | Remove a user                |

The client also displays the **raw HTTP request and response** for each operation, helping you understand what happens "under the hood."

### Architecture with Client

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                      Complete REST Architecture                             │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────────────┐         HTTP Request          ┌─────────────────┐  │
│  │                     │  ───────────────────────────► │                 │  │
│  │   client.html       │    GET /users                 │   Flask API     │  │
│  │   (Browser)         │    POST /users                │   (app.py)      │  │
│  │                     │    PUT /users/1               │                 │  │
│  │   JavaScript        │    DELETE /users/1            │   Port 8000     │  │
│  │   fetch() API       │  ◄─────────────────────────── │                 │  │
│  │                     │         JSON Response         │                 │  │
│  └─────────────────────┘                               └─────────────────┘  │
│                                                                             │
│  The browser enforces CORS policy:                                          │
│  • Same origin → allowed                                                    │
│  • Different origin → blocked unless server sends CORS headers              │
│  • flask-cors adds: Access-Control-Allow-Origin: *                          │
│                                                                             │
├─────────────────────────────────────────────────────────────────────────────┤
│  Local:  client.html (file://) ──► http://localhost:8000                    │
│  Azure:  client.html (file://) ──► https://yourapp.azurewebsites.net        │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Homework (Self-Study)

To better understand how a REST API is built with Flask, go through the source code in **`app.py`** and complete the following:

1. **Trace the Code**
   - Identify where the Flask app is created.
   - Locate the routes (`/users`, `/users/<id>`) and note which HTTP methods each supports.
   - See how data is stored (in-memory) and how JSON is returned.

2. **Test the Endpoints**
   - Run the app locally and use `test-api.http` or `curl` to try all CRUD operations.
   - Observe the status codes (200, 201, 404, etc.) and responses.

3. **Reflect**
   - Make sure you are able to describe how a request like `POST /users` flows:
     - From the request body → Flask route → data store → JSON response.

4. **Optional Enhancement**
   - Add one small improvement (e.g., input validation, error handling, or duplicate ID check).
   - Test your change with a sample request.

This is not a graded activity.

