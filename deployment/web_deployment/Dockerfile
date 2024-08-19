FROM python:3.12-slim


WORKDIR /app

COPY deployment/web-deployment/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY deployment/web-deployment/app.py deployment/web-deployment/model.pkl ./

EXPOSE 8501

CMD ["streamlit", "run", "app.py", "--server.port=8080", "--server.headless=true"]