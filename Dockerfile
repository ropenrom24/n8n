FROM n8nio/n8n:latest

USER root

# Install Python, virtualenv, and ffmpeg
RUN apk add --no-cache python3 py3-pip py3-virtualenv ffmpeg && \
    python3 -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir yt-dlp && \
    apk del py3-pip && \
    rm -rf /var/cache/apk/*

# Add yt-dlp and ffmpeg to PATH
ENV PATH="/opt/venv/bin:$PATH"

# Copy your script into the container
COPY yt.py /usr/local/bin/yt.py
RUN chmod +x /usr/local/bin/yt.py

USER node
