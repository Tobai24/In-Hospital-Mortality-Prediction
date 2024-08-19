# Deploying Your Model Locally ✨

Ready to get your model up and running locally? Follow these easy steps:

### **Create or Activate Your Pipenv Environment:**

   If you haven’t set up a Pipenv environment yet, you can do so by running:

   If you have already actiavted the pipenv/virtual environment as in the Setup you can skip this step

   ```bash
   pip install pipenv
   ```

   If you already have Pipenv environment installed, activate it with:
   ```bash
   pipenv install
   pipenv shell
   ```

   This ensures all the required dependencies are installed for your project. Check the `Pipfile` for a list of dependencies used.

### **Package the App into Docker:**

   The prediction script has been embedded into a Flask application and packed into a Docker image. To build the Docker image, run:

   ```bash
   docker build -t mortality-prediction:v1 .
   ```

### **Run the Docker Container:**

   Once the Docker image is built, you can run it locally with:

   ```bash
   docker run -it -p 9696:9696 mortality-prediction:v1
   ```

   This command will start the container and expose it on port `9696`. You can access your Flask app at `http://localhost:9696`.

### **Use the Flask App for Predictions:**

   To use the Flask app for predictions, you need to run `test.py`. you can change the content of the test.py to see the output for each value.

Feel free to check the `test.py` file for more details on how the script and Flask app are set up. If you have any questions or need further assistance, just let me know. Happy deploying! 🎉