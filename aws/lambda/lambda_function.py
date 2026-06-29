import json

from aws_secrets import get_secret
from snowflake_client import SnowflakeClient


def lambda_handler(event, context):

    client = None

    try:

        credentials = get_secret()

        client = SnowflakeClient(credentials)
        client.connect()

        # Manual test from Lambda console
        if "Records" not in event:
            result = client.run_customer_etl()

        else:
            key = event["Records"][0]["s3"]["object"]["key"]

            print(f"Uploaded File: {key}")

            if key.startswith("raw/customers/"):
                result = client.run_customer_etl()

            elif key.startswith("raw/products/"):
                result = client.run_product_etl()

            elif key.startswith("raw/sales/"):
                result = client.run_sales_etl()

            else:
                return {
                    "statusCode": 200,
                    "body": json.dumps({
                        "status": "IGNORED",
                        "message": f"No pipeline configured for {key}"
                    })
                }

        return {
            "statusCode": 200,
            "body": json.dumps({
                "status": "SUCCESS",
                "message": result
            })
        }

    except Exception as e:

        return {
            "statusCode": 500,
            "body": json.dumps({
                "status": "FAILED",
                "message": str(e)
            })
        }

    finally:
        if client:
            client.close()