#!/bin/bash

docker build . -t sssimp
docker run -v output:/app/output sssimp
