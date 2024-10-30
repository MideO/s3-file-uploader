from s3fileuploader.config.aws import AwsConfig


def test_aws_config_with_defaults():
    config = AwsConfig()
    assert config.region is None
    assert config.endpoint is None
