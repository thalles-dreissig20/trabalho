from datetime import datetime

class Validator:
    def validate_data(data_str):
        try:
            date_part = datetime.strptime(data_str, "%d-%m-%Y").date()
            return date_part
        except ValueError:
            print("Data inválida. Use o formato DD-MM-YYYY.")
            return None

    def validate_cnpj(cnpj_str):
        cleaned_cnpj = cnpj_str.replace(".", "").replace("-", "").replace("/", "")
        if len(cleaned_cnpj) != 14 or not cleaned_cnpj.isdigit():
            print("CNPJ inválido. Use o formato XX.XXX.XXX/XXXX-XX.")
            return None
        return cleaned_cnpj