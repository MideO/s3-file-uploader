from moto import mock_aws

from s3fileuploader.dao import aws


@mock_aws
def test_s3():
    s3 = aws._s3(region_name="us-east-1", endpoint_url=None)
    bucket = "bucket"
    key = "key"
    content = "some content in the file"
    s3.create_bucket(Bucket=bucket)

    s3.put_object(Bucket=bucket, Key=key, Body=content)

    body = s3.get_object(Bucket=bucket, Key=key)["Body"].read().decode("utf-8")
    assert body == content
