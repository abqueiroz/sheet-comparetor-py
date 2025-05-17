from typing import List, Union, Optional, Dict
import gspread
from google.oauth2.service_account import Credentials

class SpreadsheetComparator:
    def __init__(self, spreadsheet_id: str, credentials: Credentials):
        self.spreadsheet_id = spreadsheet_id
        self.credentials = credentials
        self.client = gspread.authorize(credentials)
        self.doc = self.client.open_by_key(spreadsheet_id)
        self.sheet = None

    def compare_column_with_array(
        self,
        column_header: str,
        expected_values: List[str],
        sheet_name_or_index: Union[str, int] = 0
    ) -> Optional[Dict[str, List[str]]]:
        try:
            if not self._load_sheet(sheet_name_or_index):
                return None

            column_values = self._extract_column_values(column_header)
            if column_values is None:
                return None

            return self._compare_values(column_values, expected_values)

        except Exception as e:
            print("Ocorreu um erro:", str(e))
            return None

    def _load_sheet(self, sheet_name_or_index: Union[str, int]) -> bool:
        try:
            if isinstance(sheet_name_or_index, int):
                worksheets = self.doc.worksheets()
                if 0 <= sheet_name_or_index < len(worksheets):
                    self.sheet = worksheets[sheet_name_or_index]
                else:
                    print(f"Índice de aba \"{sheet_name_or_index}\" inválido.")
                    return False
            elif isinstance(sheet_name_or_index, str):
                try:
                    self.sheet = self.doc.worksheet(sheet_name_or_index)
                except gspread.WorksheetNotFound:
                    print(f"Aba com o nome \"{sheet_name_or_index}\" não encontrada.")
                    return False
            else:
                print("Fallback para a primeira aba.")
                self.sheet = self.doc.get_worksheet(0)
            return True
        except Exception as e:
            print(f"Erro ao carregar aba: {e}")
            return False

    def _extract_column_values(self, column_header: str) -> Optional[List[str]]:
        try:
            if self.sheet is None:
                return None

            headers = self.sheet.row_values(1)
            if column_header not in headers:
                print(f"Coluna com o header \"{column_header}\" não encontrada.")
                return None

            column_index = headers.index(column_header) + 1
            values = self.sheet.col_values(column_index)[1:]

            column_values = []
            for value in values:
                if not value.strip():
                    print("Linha vazia encontrada. Interrompendo a leitura.")
                    break
                column_values.append(value.strip())

            return column_values
        except Exception as e:
            print(f"Erro ao extrair coluna: {e}")
            return None

    def _compare_values(self, sheet_values: List[str], expected_values: List[str]) -> Dict[str, List[str]]:
        missing_in_expected = [val for val in sheet_values if val not in expected_values]
        missing_in_sheet = [val for val in expected_values if val not in sheet_values]
        return {
            "missingInExpected": missing_in_expected,
            "missingInSheet": missing_in_sheet
        }
