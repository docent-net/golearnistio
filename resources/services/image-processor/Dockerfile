FROM registry.fedoraproject.org/fedora-minimal:32
RUN microdnf install -y python python-pip && microdnf clean all
RUN useradd -ms /bin/bash service-user

USER service-user
RUN mkdir /home/service-user/bin

ADD requirements.txt /home/service-user/requirements.txt
ADD app.py /home/service-user/bin/app.py
RUN pip install --user -r /home/service-user/requirements.txt

ENTRYPOINT ["python", "/home/service-user/bin/app.py"]