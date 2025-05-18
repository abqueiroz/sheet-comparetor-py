import requests
import csv
from io import StringIO
from typing import List, Dict, Optional


class PublicSpreadsheetComparator:
    def __init__(self, spreadsheet_id: str, gid: str = "0"):
        self.spreadsheet_id = spreadsheet_id
        self.gid = gid

    def compare_column_with_array(self, column_header: str, expected_values: List[str]) -> Optional[Dict[str, List[str]]]:
        try:
            csv_data = self._fetch_csv_data()
            reader = csv.DictReader(StringIO(csv_data))
            column_values = [row[column_header] for row in reader if column_header in row]

            if not column_values:
                print(f'Coluna "{column_header}" não encontrada.')
                return None

            return self._compare_values(column_values, expected_values)
        except Exception as e:
            print(f"Erro ao comparar planilha pública: {e}")
            return None

    def _fetch_csv_data(self) -> str:
        url = f"https://docs.google.com/spreadsheets/d/{self.spreadsheet_id}/gviz/tq?tqx=out:csv&gid={self.gid}"
        response = requests.get(url)
        response.raise_for_status()
        return response.text

    def _compare_values(self, sheet_values: List[str], expected_values: List[str]) -> Dict[str, List[str]]:
        missing_in_expected = [v for v in sheet_values if v not in expected_values]
        missing_in_sheet = [v for v in expected_values if v not in sheet_values]
        return {
            "missingInExpected": missing_in_expected,
            "missingInSheet": missing_in_sheet
        }