import argparse
import json
from google.oauth2.service_account import Credentials
from spreadsheet_comparator import SpreadsheetComparator

def main():
    parser = argparse.ArgumentParser(description="Compara valores de uma coluna de uma planilha Google Sheets com uma lista esperada.")
    parser.add_argument("spreadsheet_id", help="ID da planilha do Google Sheets")
    parser.add_argument("column_header", help="Cabeçalho da coluna a ser comparada")
    parser.add_argument("expected_values", help="Valores esperados (em JSON ou separados por vírgula)")
    parser.add_argument("--sheet", help="Nome ou índice da aba (padrão: 0)", default=0)
    parser.add_argument("--credentials", help="Caminho para o arquivo de credenciais JSON", default="credentials.json")

    args = parser.parse_args()

    try:
        # Autentica com google-auth
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive']
        credentials = Credentials.from_service_account_file(args.credentials, scopes=SCOPES)

        # Lê lista esperada (como JSON ou string separada por vírgula)
        try:
            expected_values = json.loads(args.expected_values)
        except json.JSONDecodeError:
            expected_values = [v.strip() for v in args.expected_values.split(",")]

        # Converte índice da aba, se for número
        sheet_selector = int(args.sheet) if args.sheet.isdigit() else args.sheet

        comparator = SpreadsheetComparator(args.spreadsheet_id, credentials)
        result = comparator.compare_column_with_array(args.column_header, expected_values, sheet_selector)

        if result:
            print(json.dumps(result, indent=2, ensure_ascii=False))
        else:
            print("Nenhum resultado ou erro ao comparar.")
    except Exception as e:
        print(f"Erro ao executar: {e}")

if __name__ == "__main__":
    main()
