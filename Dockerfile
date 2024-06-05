FROM python:3.10-alpine
WORKDIR /World Of Games
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY  . .
CMD ["flask", "run"]