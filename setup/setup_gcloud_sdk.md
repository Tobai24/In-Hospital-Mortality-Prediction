### 📋 **Prerequisite 4: Installing Google Cloud SDK**

1. **Download and Install Google Cloud SDK**:

   - Visit the [Google Cloud SDK installation page](https://cloud.google.com/sdk/docs/install).
   - Choose your platform and follow the instructions:
     - **Windows**: Download and run the installer.
     - **Mac/Linux**: Use the following command in your terminal:

       ```bash
       curl https://sdk.cloud.google.com | bash
       exec -l $SHELL
       ```

2. **Initialize the SDK**:

   - Run the following command to initialize the Google Cloud SDK:

     ```bash
     gcloud init
     ```

   - Follow the prompts to log in to your Google account and set up the default project.

3. **Verify Installation**:

   ```bash
   gcloud --version
   ```