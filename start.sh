#!/bin/bash
export DB_HOST=""
export DB_USERNAME=""
export DB_PASSWORD=""
export DB_NAME=""
export DB_PORT=""
export SCHEMA=""
echo "Starting server on localhost port 8000"
uvicorn main:app --reload
