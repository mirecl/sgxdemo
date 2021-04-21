gunicorn \
    -w 4 \
    -b:8080 \
    --max-requests 10000 \
    --max-requests-jitter 1000 \
    --log-level info \
    --access-logfile - \
    server:app