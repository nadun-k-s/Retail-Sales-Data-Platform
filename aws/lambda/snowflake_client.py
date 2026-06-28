import snowflake.connector


class SnowflakeClient:

    def __init__(self, credentials):
        self.credentials = credentials
        self.connection = None

    def connect(self):
        self.connection = snowflake.connector.connect(
            user=self.credentials["user"],
            password=self.credentials["password"],
            account=self.credentials["account"],
            warehouse=self.credentials["warehouse"],
            database=self.credentials["database"],
            schema=self.credentials["schema"],
            role=self.credentials["role"]
        )
        return self.connection

    def execute(self, sql):
        cursor = self.connection.cursor()
        try:
            cursor.execute(sql)
            return cursor.fetchall()
        finally:
            cursor.close()

    def run_etl(self):
        return self.execute("CALL RETAIL_DW.CONTROL.SP_RUN_FULL_ETL();")

    def get_version(self):
        return self.execute("SELECT CURRENT_VERSION();")

    def close(self):
        if self.connection:
            self.connection.close()