FROM python:3.8-slim-buster

WORKDIR /benford_project

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./benford_api ./benford_api
COPY ./benford_plot ./benford_plot
ENV PYTHONPATH "${PYTHONPATH}:/benford_project/"

CMD ["python", "./benford_api/app.py"]