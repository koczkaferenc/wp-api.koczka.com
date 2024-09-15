FROM python:3

ARG PORT
ENV PORT=${PORT}

RUN mkdir /app
WORKDIR /app
# ------------
# ADD . .
ADD requirements.txt /app
RUN pip install -r requirements.txt
EXPOSE ${PORT}
CMD ["python3","app.py"]