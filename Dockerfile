FROM pytorch/pytorch:1.11.0-cuda11.3-cudnn8-runtime

ENV LANG C.UTF-8

WORKDIR /app

COPY . .
RUN apt-get update
RUN apt-get install ffmpeg libsm6 libxext6  -y
RUN pip3 install -r requirements.txt

CMD ["python3", "bird_repellen_docker.py"]
