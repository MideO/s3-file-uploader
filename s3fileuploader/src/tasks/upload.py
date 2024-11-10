import logging
import os
from typing import Callable

from boto.s3.connection import S3Connection
from botocore.exceptions import ClientError
from celery import Task

from utils.lock import Lock

LOG = logging.getLogger("app")


class UploadTask(Task):
    def __init__(self, s3: S3Connection, lock_provider: Callable[[str], Lock]):
        self.name = "AwsS3Service"
        self.s3: S3Connection = s3
        self.lock_provider = lock_provider

    def run(self, *args, **kwargs):
        path, filename, bucket = args
        with self.lock_provider(filename):
            try:
                self.s3.head_bucket(Bucket=bucket)
            except ClientError:
                self.s3.create_bucket(Bucket=bucket)
            LOG.info("Uploading file %s", filename)
            self.s3.upload_file(path, bucket, filename)
            os.remove(path)
            LOG.info("Uploaded file %s successfully", filename)
