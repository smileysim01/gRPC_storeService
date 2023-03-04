FROM ubuntu:20.04


RUN apt-get update

RUN apt-get install -y python3 python3-pip curl lsof

RUN pip3 install jupyterlab==3.4.5 MarkupSafe==2.0.1

CMD ["python3", "-m", "jupyterlab", "--no-browser", "--ip=0.0.0.0", "--port=5440", "--allow-root", "--NotebookApp.token=''"]
