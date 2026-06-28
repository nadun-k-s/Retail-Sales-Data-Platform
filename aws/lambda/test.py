print("Starting test...")

from aws_secrets import get_secret

print("Imported successfully")

secret = get_secret()

print("Secret retrieved:")
print(secret)

print("Finished")