from io import BytesIO
from typing import Callable

from boto.s3.connection import S3Connection

from ..utils.lock import Lock


class AwsS3Service:
    def __init__(self, s3: S3Connection, lock_provider: Callable[[str], Lock]):
        self.s3: S3Connection = s3
        self.lock_provider = lock_provider

    def upload_file(self, content: BytesIO, filename: str, bucket: str):
        with self.lock_provider(filename):
            self.s3.upload_fileobj(content, bucket, filename)
