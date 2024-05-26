FROM python:3.11

WORKDIR /tmp

# Add in python requirements
COPY requirements.txt .
RUN pip install -r requirements.txt

# Add in application - most likely to change so add near end
ADD app /usr/local/app

# Ensure App Location is in python path
ENV PYTHONPATH "${PYTHONPATH}:/usr/local/app"

# Placeholder command
CMD ["python", "--version"]
