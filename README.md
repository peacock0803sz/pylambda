# pylambda

## Steps to deploy

1. Copy pylambda/\_config.yaml to pylambda/config.yaml, and Dockerfile also.
2. Set `region`, `bucket_name`, `s3_key_prefix`, `aws_access_key_id`, `aws_secret_access_key` in config.yaml
3. Set `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_DEFAULT_REGION` in Dockerfile
4. Run `docker build -t pylambda .` and `docker run -it --rm -v $(pwd):/app pylambda`

