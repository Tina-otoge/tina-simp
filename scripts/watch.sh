#!/bin/bash

./scripts/run.sh
./scripts/exit_on_change.py .2
exec ./scripts/watch.sh
