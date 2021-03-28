FROM docker.io/library/golang:1.16 as builder
RUN mkdir -p /tmp/workdir

ADD main.go /tmp/workdir/main.go
WORKDIR /tmp/workdir
RUN go build main.go

FROM registry.fedoraproject.org/fedora-minimal:32
RUN useradd -ms /bin/bash service-user

USER service-user
RUN mkdir /home/service-user/bin

COPY --from=builder --chown=service-user /tmp/workdir/main /home/service-user/bin/service

ENTRYPOINT ["/home/service-user/bin/service"]