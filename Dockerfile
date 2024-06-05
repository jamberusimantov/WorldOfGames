FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3 python3-pip curl
COPY .. /WorldOfGames
WORKDIR /WorldOfGames
RUN pip install -r requirements.txt
RUN mv Scores.txt /Scores.txt
ENV FLASK_APP=app
EXPOSE 5000
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5000", "--debug"]