# 💻 Portable Remote Development Station

![VS Code](https://img.shields.io/badge/VS%20Code-007ACC?style=for-the-badge&logo=visual-studio-code&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?style=for-the-badge&logo=c%2B%2B&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)

> A production-ready, containerized Integrated Development Environment (IDE) accessible via any web browser. Designed to standardize tooling across devices and provide seamless access to NAS-hosted projects.

---

## 📖 Overview

This repository defines a **Development-as-Code** environment. Instead of manually installing compilers and tools on every new laptop or tablet, this setup deploys a fully configured VS Code Server instance inside a Docker container.

It bridges the gap between local comfort and remote power, allowing for:
* **Consistency:** The exact same GCC version and Python libraries, everywhere.
* **Portability:** Code from an iPad, a low-power laptop, or a library computer.
* **Centralization:** All source code and data remain securely stored on the NAS, never synced to temporary devices.

---

## ⚡ Tech Stack & Features

| Component | Technology | Description |
| :--- | :--- | :--- |
| **Core IDE** | [code-server](https://github.com/coder/code-server) | VS Code running on a remote server, accessible via HTTP. |
| **Container** | [Docker](https://www.docker.com/) | Isolates the dev environment from the host OS. |
| **Languages** | Python 3, C++ | Pre-installed compilers (GCC/G++) and interpreters. |
| **Version Control** | Git | Integrated terminal access for full Git workflows. |
| **Storage** | Bind Mounts | Direct access to the host's physical project directories. |

### 🛠️ Pre-Installed Toolchain
The container automatically provisions the following tools on startup:
* **Python 3.x** + `pip`
* **Build Essentials:** `make`, `gcc`, `g++`, `gdb`
* **Git** for version control
* **Sudo** privileges for package management (`apt`)

---

## 🚀 Deployment Guide

### 1. Prerequisites
* A server or NAS running **Docker Engine** & **Docker Compose**.
* (Optional) **Tailscale** for secure remote access without port forwarding.

### 2. Installation
Clone the repository to your host machine:
```bash
git clone [https://github.com/kimzam30/RemoteDevSetupWithNAS.git](https://github.com/kimzam30/RemoteDevSetupWithNAS.git)
cd RemoteDevSetupWithNAS
```
### 3. Configuration
Create the environment file. This is critical for security and permissions.
```Bash
cp .env.example .env
```
Open .env and configure your settings:
```
# User Permissions (Run 'id' on host to find these)
PUID=1000
PGID=1000

# Security
PASSWORD=secure_dev_password

# Host Paths
PROJECTS_ROOT=/home/kimzam30/projects  # Where your actual code lives
```
### 4. Launch
Spin up the environment:

```bash
docker-compose up -d
```
## 🌐 Secure Remote Access (Tailscale)

This environment is designed to be accessed via **Tailscale**, a private mesh VPN. This allows you to connect securely from anywhere (coffee shop, hotel, etc.) without opening ports on your router.

### How to Connect
1.  **Host Side:** Ensure Tailscale is running on your NAS/Server.
    * *Tip:* Run `tailscale ip` on your host to find its private IP (starts with `100.x.x.x`).
2.  **Client Side:** Install the Tailscale app on your remote device (iPad, Laptop, Phone).
3.  **Access:** Open your browser and navigate to:
    ```
    http://<YOUR-TAILSCALE-IP>:8443
    ```
    *(Example: `http://100.86.212.92:8443`)*

> **Security Note:** Because we bind the service to `0.0.0.0` in Docker, it is technically accessible on your local network too. Using Tailscale ensures you can access it safely even when you are miles away.

## 🖥️ Usage

- Access: Navigate to http://<your-server-ip>:8443 in your browser.
- Login: Enter the password defined in your .env file.

Develop:

- Your project files are available in the /home/coder/project directory.

- Open the integrated terminal (Ctrl+`) to run python or g++ commands.

### **Installing Extensions**
Extensions install directly from the Open VSX Registry.
- Python: Search for "Python" and install the Microsoft extension.
- C++: Search for "C/C++" (IntelliSense).

***Note: Extensions and user settings are persisted in the config/ folder on your host, so they survive container restarts.***

## 📂 Directory Structure
```
RemoteDevSetupWithNAS/
├── config/
│   └── code-server/      # Persistent data (Extensions, User Settings)
├── .env.example          # Configuration template
├── .gitignore            # Security rules
└── docker-compose.yaml   # Container definition
```
## 🤝 Contributing

This is a personal development environment, but forks and suggestions are welcome.

1. Fork the Project
2. Create your Feature Branch (git checkout -b feature/NewTool)
3. Commit your Changes (git commit -m 'Add Golang support')
4. Push to the Branch (git push origin feature/NewTool)
5. Open a Pull Request
#
maintained by kimzam