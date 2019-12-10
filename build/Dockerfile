ARG APP_PROJECT=job_automation

FROM python:3

WORKDIR /app/$APP_PROJECT

COPY ./$APP_PROJECT .
RUN pip3 install --requirement ./requirements.txt

CMD ["sleep", "infinity"]
