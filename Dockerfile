FROM ubuntu:22.04
RUN apt update && apt install python3 git 
WORKDIR travel
COPY . .
RUN pip install -r requirements.txt
CMD ["python3","travel.py"]
