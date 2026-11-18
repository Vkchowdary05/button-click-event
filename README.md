# Project 15: Button Click Event

> **DevOps External Exam / Lab Assignment**
> - **15.a:** Create a simple HTML webpage with a button that displays an alert message when clicked. Upload the source code to GitHub using Git.
> - **15.b:** Use Selenium to automate button-click testing and deploy a sample application using Kubernetes.

---

## 1. Project Overview & Features
- **Frontend:** Pure HTML5, modern monochrome CSS3 (shadcn-inspired black & white theme), and Vanilla JavaScript.
- **Interactive Event:** Interactive button triggering `window.alert()` with configurable/default message, updating click counter and event telemetry.
- **Containerization:** Production-ready `Dockerfile` based on `nginx:alpine`.
- **Orchestration:** Kubernetes manifests (`deployment.yaml` with 2 replicas and health checks, `service.yaml` with NodePort `30015`).
- **Automated QA:** Automated Selenium WebDriver test suite that launches headless Chrome, clicks the button, intercepts and verifies the JavaScript alert popup, accepts it, and asserts DOM telemetry state.

---

## 2. Project Structure
```text
15-button-click-event/
├── index.html                 # Webpage with alert trigger button and telemetry
├── style.css                  # Minimalist black & white stylesheet
├── app.js                     # JavaScript click event handler and state updates
├── Dockerfile                 # Container definition using Nginx Alpine
├── k8s/
│   ├── deployment.yaml        # Kubernetes 2-replica deployment manifest
│   └── service.yaml           # Kubernetes NodePort service manifest (Port 30015)
├── tests/
│   ├── test_button_click.py   # Automated Selenium alert test script
│   └── requirements.txt       # Python testing dependencies
├── setup_git.bat              # Automated Git initialization script (Windows)
├── .gitignore                 # Files ignored by Git
└── README.md                  # Documentation and execution guide
```

---

## 3. Source Code Management with Git and GitHub (15.a)

### Step 1: Initialize Local Git Repository
Run `setup_git.bat` or run the following in terminal:
```bash
git init
git add .
git commit -m "feat: initial commit for Project 15 Button Click Event"
```

### Step 2: Push to GitHub
1. Create a repository on [GitHub](https://github.com/new) named `button-click-event`.
2. Connect your local repository and push:
```bash
git branch -M main
git remote add origin https://github.com/<YOUR_GITHUB_USERNAME>/button-click-event.git
git push -u origin main
```

---

## 4. Local Execution
Open `index.html` directly in any web browser, or serve it using Python's built-in HTTP server:
```bash
# From inside 15-button-click-event directory
python -m http.server 8000
```
Open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 5. Automated Button-Click Testing using Selenium (15.b)

The test suite automatically tests the webpage using headless Google Chrome.

### Prerequisites:
```bash
pip install -r tests/requirements.txt
```

### Run Tests:
```bash
# Test against local index.html directly:
python tests/test_button_click.py

# Or test against running Kubernetes/Docker service:
python tests/test_button_click.py --url http://localhost:8080
```

### Automated Checks Performed:
1. **Page Title:** Validates that `<title>` contains "Button Click Event".
2. **Button Presence:** Ensures `#alert-button` is visible and interactable.
3. **Alert Trigger & Interception:** Clicks the button, intercepts `window.alert()` via `driver.switch_to.alert`, verifies message text `"Button was clicked successfully"`, and accepts the alert.
4. **Counter Increment:** Confirms the `#click-count` in the DOM increments to `1`.
5. **Multiple Click Flow:** Executes a second click, accepts alert, and verifies count becomes `2`.
6. **Reset Action:** Clicks `#reset-button` and confirms counter restores to `0`.

---

## 6. Deploying on Kubernetes (15.b)

### Step 1: Build Docker Image
```bash
docker build -t button-click-app:latest .
```

### Step 2: Apply Kubernetes Manifests
```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Step 3: Verify Pods and Service
```bash
kubectl get pods -l app=button-click-app
kubectl get service button-click-service
```

### Step 4: Access Application
- **Via Port Forwarding:**
  ```bash
  kubectl port-forward svc/button-click-service 8080:80
  ```
  Visit [http://localhost:8080](http://localhost:8080).
- **Via NodePort:**
  Visit `http://<CLUSTER_NODE_IP>:30015`.
