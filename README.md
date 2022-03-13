# dockerize-flask-app
Dockerize Simple Flask Application

## Requirements
- Docker

## Building the Project

Clone the repository and `cd` in it:
```bash
git clone https://github.com/isakilikya/dockerize-flask-app.git
cd dockerize-flask-app
```

Create image by building Dockerfile:
```bash
docker image build -t isakilikya/dockerize-flask-app .
```

Run container:
```bash
docker container run -d -p 5000:5000 isakilikya/dockerize-flask-app
```

Project:
```
http://localhost:5000
```

