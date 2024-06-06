FROM python:3.12-alpine3.20
WORKDIR /WorldOfGames
# Install dependencies
RUN apk add --no-cache gcc musl-dev linux-headers
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install -r requirements.txt
# Copy source files into application directory
COPY . .
RUN mv Scores.txt /Scores.txt
CMD ["flask", "run"]