FROM python:3.13.5-slim
WORKDIR /docker


# Install the application dependencies
COPY requirements.txt ./
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy in the source code
COPY . .

EXPOSE 5000

CMD [ "flask","--app" ,"loantap","run","--host=0.0.0.0", "--port=5000"]