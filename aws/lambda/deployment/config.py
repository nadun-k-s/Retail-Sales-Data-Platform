"""
Application configuration.

All configurable values are defined here so they can be changed
without modifying the application logic.
"""

# AWS Configuration
AWS_REGION = "eu-north-1"
SECRET_NAME = "ETL_SERVICE"

# Snowflake Configuration
SNOWFLAKE_PROCEDURE = "CALL RETAIL_DW.CONTROL.SP_RUN_FULL_ETL();"

# Application
APPLICATION_NAME = "Retail Snowflake ETL"
APPLICATION_VERSION = "1.0.0"