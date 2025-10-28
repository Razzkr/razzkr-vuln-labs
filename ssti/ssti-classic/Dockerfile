FROM python:3

# system deps
RUN apt update -y && apt install -y --no-install-recommends supervisor \
 && rm -rf /var/lib/apt/lists/*

# python deps
RUN pip install --no-cache-dir flask debugpy

# app
WORKDIR /app
COPY vsnippet/ /app/
COPY config/supervisord.conf /etc/supervisord.conf

# strip UTF-8 BOM + CRLF from supervisor config (Windows-safe)
RUN python - <<'PY'
from pathlib import Path
p = Path('/etc/supervisord.conf'); b = p.read_bytes()
if b.startswith(b'\xef\xbb\xbf'): b = b[3:]
b = b.replace(b'\r\n', b'\n').replace(b'\r', b'\n')
p.write_bytes(b)
print('Sanitized /etc/supervisord.conf')
PY

ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
EXPOSE 5000 5678
CMD ["/usr/bin/supervisord","-c","/etc/supervisord.conf"]

