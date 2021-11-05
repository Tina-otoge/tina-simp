#!/bin/bash

python -m venv .venv
source ./.venv/bin/activate
(cd ../sssimp && pip install .) || pip install --upgrade sssimp
python -m sssimp
