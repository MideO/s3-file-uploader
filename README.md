## What is it?
##### Python/FastAPI application to save and delete AWS S3 files via celery tasks.
##### A redis lock is used to handle concurrency across multiple instances 

![workflow](https://github.com/MideO/s3-file-uploader/actions/workflows/ci.yml/badge.svg)

## TODO
 - Upload
   - [x] UI 
   - [x] Celery Task
 - List
   - [ ] UI
   - [ ] Celery Task
 - Download
   - [ ] UI
   - [ ] Celery Task
 - Delete
   - [ ] UI
   - [ ] Celery Task
 

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
├── pytest.ini
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


