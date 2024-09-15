FROM python:3
ARG PORT
RUN mkdir /app
WORKDIR /app
ADD . .
RUN pip install -r requirements.txt
EXPOSE ${PORT}
CMD ["python3","app.py"]