#!/bin/bash
docker build -t domo-dht-manager .
docker run --rm --name=domo-dht-manager -it -p 3000:3000 domo-dht-manager 

