#!/bin/bash

cd input/content/scripts
brython-cli --install
brython-cli --modules
rm -v demo.html index.html README.txt unicode.txt brython_stdlib.js
cd ..
mkdir -p assets/js/brython
mv -v scripts/{brython.js,brython_modules.js} assets/js/brython
