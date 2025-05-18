import csv
from typing import List, Dict, Optional


class LocalCsvComparator:
    def __init__(self, file_path: str):
        self.file_path = file_path

    def compare_column_with_array(self, column_header: str, expected_values: List[str]) -> Optional[Dict[str, List[str]]]:
        try:
            with open(self.file_path, mode='r', encoding='utf-8') as file:
                reader = csv.DictReader(file)
                column_values = [row[column_header] for row in reader if column_header in row]

            if not column_values:
                print(f'Coluna "{column_header}" não encontrada no arquivo.')
                return None

            return self._compare_values(column_values, expected_values)
        except Exception as e:
            print(f"Erro ao comparar CSV local: {e}")
            return None

    def _compare_values(self, sheet_values: List[str], expected_values: List[str]) -> Dict[str, List[str]]:
        missing_in_expected = [v for v in sheet_values if v not in expected_values]
        missing_in_sheet = [v for v in expected_values if v not in sheet_values]
        return {
            "missingInExpected": missing_in_expected,
            "missingInSheet": missing_in_sheet
        }
