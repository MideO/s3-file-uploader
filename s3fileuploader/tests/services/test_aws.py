import io
from unittest.mock import patch, MagicMock

import pytest
from moto import mock_aws

from s3fileuploader.src.clients import aws
from s3fileuploader.src.services.aws import AwsS3Service
from s3fileuploader.src.utils.lock import Lock

pytest.locks = {}


def insert_lock_side_effect(name, value, **kwargs):
    pytest.locks[name] = value


def delete_lock_side_effect(name):
    del pytest.locks[name]


@pytest.fixture(autouse=True)
def clear_lock():
    pytest.locks = {}


@mock_aws
def test_upload_file():
    redis = MagicMock()
    redis.set.side_effect = insert_lock_side_effect
    redis.delete.side_effect = delete_lock_side_effect
    redis.get.side_effect = lambda _: None
    s3 = aws.s3_client(region_name="us-east-1", endpoint_url=None)
    service = AwsS3Service(s3, lambda x: Lock(x, redis))
    bucket = "bucket"
    key = "key"

    content = b"my data stored as file object in RAM"
    s3.create_bucket(Bucket=bucket)
    obj = io.BytesIO(content)
    service.upload_file(obj, key, bucket)

    body = s3.get_object(Bucket=bucket, Key=key)["Body"].read()
    assert body == content
