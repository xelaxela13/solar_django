import multiprocessing

# Turn on debugging in the server. [False]
debug = False

# Install a trace function that spews every line executed by the server. [False]
spew = False

# The Access log file to write to. [None]
# accesslog='/var/log/gunicorn.access.log'

# The Access log format . [%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"]
# access_log_format='"%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'

# Logging config file.
# logconfig = "/opt/example/log.conf"

# The Error log file to write to. [-]
# errorlog="/var/log/gunicorn.log"

# The granularity of Error log outputs. [info]
loglevel = 'debug'

# The logger you want to use to log events in gunicorn. [simple]
# logger_class='simple'

# A base to use with setproctitle for process naming. [None]
proc_name = 'solar_django'

# Load application code before the worker processes are forked. [False]
preload = True

# forked. [False]
# daemon=False
# daemon = True

# A filename to use for the PID file. [None]
# pidfile = '/var/run/example.pid'

# Switch worker processes to run as this user. [0]
# user = "root"

# Switch worker process to run as this group. [0]
# group = "root"

# A bit mask for the file mode on files written by Gunicorn. [0]
# umask = 0o002

# The socket to bind. [127.0.0.1:8000]
bind = 'localhost:5000'

# The maximum number of pending connections.     [2048]
#  - Amazon Linux default=1024 ($ sysctl net.ipv4.tcp_max_syn_backlog)
# backlog = 2048

# The number of worker process for handling requests. [1]
workers = multiprocessing.cpu_count() * 2 + 1
# workers=1

# The type of workers to use. [sync]
worker_class = 'sync'

# The maximum number of simultaneous clients. [1000]
# worker_connections = 4098

# The maximum number of requests a worker will process before restarting. [0]
# max_requests = 4098

# Workers silent for more than this many seconds are killed and restarted. [30]
timeout = 120

# The number of seconds to wait for requests on a Keep-Alive connection. [2]
keepalive = 2

# Timeout for graceful workers restart.
graceful_timeout = 30

# The maximum size of HTTP request line in bytes.
# limit_request_line = 0

# Limit the number of HTTP headers fields in a request.
# limit_request_fields=100

# Limit the allowed size of an HTTP request header field.
# limit_request_field_size=8190
