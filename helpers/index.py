from datetime import datetime

class Validator:
    def validate_data(data_str):
        try:
            date_part = datetime.strptime(data_str, "%d-%m-%Y").date()
            return date_part
        except ValueError:
            print("Data inválida. Use o formato DD-MM-YYYY.")
            return None