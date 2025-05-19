from datetime import datetime

def validate_data(data_str):
    try:
        date_part = datetime.strptime(data_str, "%d-%m-%Y").date()
        now = datetime.now()
        combined = datetime.combine(date_part, now.time())
        return combined
    except ValueError:
        print("Data inválida. Use o formato DD-MM-YYYY.")
        return None