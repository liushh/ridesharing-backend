#!/bin/bash

${BIN_DIR}/alembic upgrade head
${BIN_DIR}/gunicorn --worker-class gthread --threads=8 -b :$PORT app:api
