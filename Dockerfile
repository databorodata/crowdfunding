FROM python:3.10

WORKDIR /dockercrowd

COPY crowd crowd

COPY requirements.txt .
COPY run.py .

RUN python -m venv /venvcrowd
ENV PATH="/venvcrowd/bin:$PATH"
RUN pip install --no-cache-dir --use-pep517 -r requirements.txt

ENV APP_SETTINGS=crowd.config.ProductionConfig
ENV DATABASE_URL=postgresql://databorodata:210243@localhost/crowd

CMD ["python", "run.py"]
