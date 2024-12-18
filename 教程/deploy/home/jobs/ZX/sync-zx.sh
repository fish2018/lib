#!/usr/bin/bash

export PATH="/usr/local/bin:$PATH"
source /home/jobs/activate
cd /home/jobs/ZX
python3 tgdown-zx.py
rm -rf ZX
