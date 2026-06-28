from aws_secrets import get_secret
from snowflake_client import SnowflakeClient

secret = get_secret()

# print(secret)

client = SnowflakeClient(secret)

client.connect()

result = client.run_etl()

print(result)

client.close()