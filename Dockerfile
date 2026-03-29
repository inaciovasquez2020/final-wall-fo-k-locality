FROM python:3.11-slim

WORKDIR /app

COPY standards/URF-SG.json standards/URF-SG.json
COPY verification/verify.py verification/verify.py

ENTRYPOINT ["python", "verification/verify.py"]
