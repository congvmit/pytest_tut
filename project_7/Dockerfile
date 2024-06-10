FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

LABEL maintainer="Cong Vo <congvm.it@gmail.com>"

COPY ./build/exe.linux-x86_64-3.10 /app

WORKDIR /app/

# COPY ./start.sh /start.sh
RUN chmod +x start.sh

ENV PYTHONPATH=/app

EXPOSE 8000

# Run the start script, it will check for an /app/prestart.sh script (e.g. for migrations)
# And then will start Gunicorn with Uvicorn
CMD ["./start.sh"]