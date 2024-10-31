from s3fileuploader.src.dependency_factory import dependencies

celery = dependencies.celery(__name__)
