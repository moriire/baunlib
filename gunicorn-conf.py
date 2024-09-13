workers = 3
command = "/home/baun/Desktop/baun-lib/.env/bin/gunicorn"
pythonpath = "/home/baun/Desktop/baun-lib/.env/bin"
#worker_class = 'uvicorn.workers.UvicornWorker'
bind = "192.168.0.100:8000"
loglevel = 'info'
graceful_timeout = 300
