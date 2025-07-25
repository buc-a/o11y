#!/bin/sh
sleep 5
python3 create_tables.py
python3 fill_tables.py
uvicorn app.main:app --host 0.0.0.0 --port 8000
