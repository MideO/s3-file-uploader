## What is it
### (WIP) Python/Flask application to upload files to S3 via a celery task and redis cache to prevent concurrent uploads of same file 

![workflow](https://github.com/MideO/s3-file-uploader/actions/workflows/ci.yml/badge.svg)

## TODO
 - Redis Locking
 - Upload, List, Download and Delete from UI
 - S3 Upload Celery Task

### Project structure:

```
.
├── .github
├── features
├── s3fileuploader
├── .coveragerc
├── .dockerignore
├── .flake8
├── .gitignore
├── app.py
├── docker-compose.yml
├── Dockerfile
├── makefile
├── pylintrc
├── README.md
├── requirements-all.txt
├── requirements-test.txt
├── requirements.txt
└── s3fileuploader
```

## How to test it
```make test```

## How to run it
```make devstack-up```

## How to stop it
```make devstack-down```


