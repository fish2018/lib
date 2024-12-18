#!/usr/bin/bash
export PATH="/usr/local/bin:$PATH"
cd /home/jobs/archive/
source venv/bin/activate
cd /home/jobs/TGForwarder
python3 TGForwarder.py
