## What is it
### (WIP) Python/FastAPI application to upload files to S3 via a celery task and redis cache to prevent concurrent uploads of same file 

![workflow](https://github.com/MideO/s3-file-uploader/actions/workflows/ci.yml/badge.svg)

## TODO
 - Upload, List, Download and Delete from UI
 - S3 Upload Celery Task

### Project structure:

```
.
├── .github
├── features    
├── .coveragerc
├── .dockerignore
├── .flake8
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── makefile
├── pylintrc
├── README.md
├── requirements-all.txt
├── requirements-test.txt
├── requirements.txt
└── s3fileuploader
    ├── src
    └── tests
```
## All available commands
```bash
make help
```

## How to test it
```bash
make test-all
```

## How to run it
```bash
make devstack-up
```

## How to stop it
```bash
make devstack-down
```


