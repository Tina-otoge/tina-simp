#!/bin/bash

source ./.venv/bin/activate
pip install pygments

pygmentize -S monokai -f html > ./input/css/pygments.css
