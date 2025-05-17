from extract_keys import (
    extract_keys
)
from google.oauth2.service_account import Credentials
from mapping import FORM_FIELD_2_SSA_PAYLOAD_CSS_WORKER_BENEFITS_INFO, FORM_FIELD_2_SSA_PAYLOAD_CSS_WORKER_TIME_OFF_INFO
from spreadsheet_comparator import SpreadsheetComparator

SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
credentials = Credentials.from_service_account_file('credentials.json', scopes=SCOPES)
spreadsheet_id = '1Z49bTwCdS6a_QG5gquooUIbUf4_8rbJNBBfd36hZI90'
comparator = SpreadsheetComparator(spreadsheet_id, credentials)

expected_values = extract_keys(FORM_FIELD_2_SSA_PAYLOAD_CSS_WORKER_BENEFITS_INFO,FORM_FIELD_2_SSA_PAYLOAD_CSS_WORKER_TIME_OFF_INFO )

resultado = comparator.compare_column_with_array(
    column_header="HEADAR_1",
    expected_values=expected_values,
    sheet_name_or_index="Sheet1"
)

print(resultado)