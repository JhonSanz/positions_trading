FROM python:3.11
RUN mkdir /app
WORKDIR /app

# VOLUME . /app
# COPY . .

COPY ./local/entrypoint ./entrypoint
RUN sed -i 's/\r$//g' ./entrypoint
RUN chmod +x ./entrypoint

COPY ./local/requirements.txt ./requirements.txt

RUN pip install -r ./requirements.txt
EXPOSE 8000
