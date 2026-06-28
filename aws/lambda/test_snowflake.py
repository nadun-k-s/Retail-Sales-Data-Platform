from secrets import get_secret
from snowflake_client import SnowflakeClient

secret = get_secret()

client = SnowflakeClient(secret)

client.connect()

result = client.execute("SELECT CURRENT_VERSION();")

print(result)

client.close()