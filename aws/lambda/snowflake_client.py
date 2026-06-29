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

    # def run_etl(self):
    #     return self.execute("CALL RETAIL_DW.CONTROL.SP_RUN_FULL_ETL();")

    def run_customer_etl(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("CALL RETAIL_DW.CONTROL.SP_PROCESS_CUSTOMER();")
            return cursor.fetchone()
        finally:
            cursor.close()


    def run_product_etl(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("CALL RETAIL_DW.CONTROL.SP_PROCESS_PRODUCT();")
            return cursor.fetchone()
        finally:
            cursor.close()


    def run_sales_etl(self):
        cursor = self.connection.cursor()
        try:
            cursor.execute("CALL RETAIL_DW.CONTROL.SP_PROCESS_SALES();")
            return cursor.fetchone()
        finally:
            cursor.close()

    # def get_version(self):
    #     return self.execute("SELECT CURRENT_VERSION();")

    def close(self):
        if self.connection:
            self.connection.close()