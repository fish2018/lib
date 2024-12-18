#!/usr/bin/bash
ps -ef | grep tdl | grep -v "grep" | awk '{print $2}' | xargs --no-run-if-empty kill

export PATH="/usr/local/bin:$PATH"
source /home/jobs/activate
cd /home/jobs/PG
python3 tgdown-pg.py
rm -rf PG
