import json

from aws_secrets import get_secret
from snowflake_client import SnowflakeClient


def lambda_handler(event, context):

    client = None

    try:

        # Read Snowflake credentials
        credentials = get_secret()

        # Connect to Snowflake
        client = SnowflakeClient(credentials)
        client.connect()

        # Execute ETL
        result = client.run_etl()

        return {
            "statusCode": 200,
            "body": json.dumps(
                {
                    "status": "SUCCESS",
                    "message": result
                },
                default=str
            )
        }

    except Exception as ex:

        return {
            "statusCode": 500,
            "body": json.dumps(
                {
                    "status": "FAILED",
                    "message": str(ex)
                }
            )
        }

    finally:

        if client:
            client.close()