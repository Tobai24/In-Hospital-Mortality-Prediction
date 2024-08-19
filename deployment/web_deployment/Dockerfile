FROM python:3.12-slim


WORKDIR /app

COPY deployment/web_deployment/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY deployment/web_deployment/app.py deployment/web_deployment/model.pkl ./

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.headless=true"]