FROM ubuntu:20.04

RUN apt-get -y  update && \
    apt-get -y install libsqlite3-dev

ADD domo-dht-manager /

ENTRYPOINT ["/domo-dht-manager", "/db.sqlite", "true", "5a52aafb2a44ff5c360d4dc04e4a792e28637da07b96072a2f0a5ea5286f2739", "3000", "false"]

