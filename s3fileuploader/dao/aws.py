import boto3

from s3fileuploader.config import app_config


def _s3(region_name: str | None, endpoint_url: str | None):
    return boto3.client(
        's3',
        region_name=region_name,
        endpoint_url=endpoint_url
    )


S3 = _s3(app_config.aws.region, app_config.aws.endpoint)
