import json
import boto3
from botocore.exceptions import ClientError

from config import AWS_REGION, SECRET_NAME


def get_secret():
    """
    Retrieve Snowflake credentials from AWS Secrets Manager.
    """

    client = boto3.client(
        "secretsmanager",
        region_name=AWS_REGION
    )

    try:
        print(f"Region: {AWS_REGION}")
        print(f"Secret Name: {SECRET_NAME}")
        response = client.get_secret_value(
            SecretId=SECRET_NAME
        )

        secret = json.loads(response["SecretString"])

        return secret

    except ClientError as e:
        raise Exception(
            f"Unable to retrieve secret: {str(e)}"
        )