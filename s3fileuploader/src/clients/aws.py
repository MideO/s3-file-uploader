import boto3
from boto.s3.connection import S3Connection


def s3_client(region_name: str | None, endpoint_url: str | None) -> S3Connection:
    return boto3.client("s3", region_name=region_name, endpoint_url=endpoint_url)
