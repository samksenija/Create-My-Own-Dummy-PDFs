import sys

sys.path.insert(0, "../connection") 

import connection_snowflake
import generate_pdf_structure

session = connection_snowflake.new_session

#I have limited data to 10 rows, as this is or testing purposes. You can remove the limit to generate PDFs for all rows in the table.
df_dummy_ledger_table= session.sql("SELECT * FROM DUMMY_DATASETS.SCHEMA_FOR_DUMMY_DATA.DUMMY_LEDGER LIMIT 10").collect()

# Generate PDFs for each row
for row in df_dummy_ledger_table:
    transaction_data = {
        "date": row[0], # This clean up will be done in dbt
        "account_description": row[1],
        "reference": row[2],
        "debit": row[3] or 0,
        "credit": row[4] or 0
    }

    generate_pdf_structure.generate_pdf(transaction_data)

session.close()