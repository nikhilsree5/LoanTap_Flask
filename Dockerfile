FROM python:3.13.5-slim-bullseye
WORKDIR /docker


# Install the application dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy in the source code
COPY . .

CMD ["python3", "-m", "flask","--app" ,"loantap","run","--host=0.0.0.0"]