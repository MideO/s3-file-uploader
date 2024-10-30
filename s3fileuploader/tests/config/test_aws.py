from s3fileuploader.config.aws import AwsConfig


def test_aws_config_with_defaults():
    config = AwsConfig()
    assert config.region == None
    assert config.endpoint == None
