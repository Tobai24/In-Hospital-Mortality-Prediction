### 📋 **Prerequisite 2: Installing Docker and Docker Compose**

1. **Install Docker**:

   - Visit the [Docker website](https://www.docker.com/get-started) and choose the installer for your operating system:
     - **Windows**: Follow [this link](https://docs.docker.com/docker-for-windows/install/).
     - **Mac**: Follow [this link](https://docs.docker.com/docker-for-mac/install/).
     - **Linux**: Use the appropriate package manager (e.g., `apt`, `yum`) based on your Linux distribution.

2. **Verify Docker Installation**:
   - Open a terminal (or PowerShell on Windows).
   - Run:

     ```bash
     docker --version
     ```

   - If installed correctly, it will display the Docker version.

3. **Install Docker Compose** (If not included with Docker):

   - **Mac and Windows**: Docker Compose comes bundled with Docker Desktop.
   - **Linux**: Install Docker Compose separately using:

     ```bash
     sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
     sudo chmod +x /usr/local/bin/docker-compose
     ```

4. **Verify Docker Compose Installation**:

   ```bash
   docker-compose --version
   ```





