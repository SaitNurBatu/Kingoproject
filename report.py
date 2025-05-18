import json

def show_report():
    try:
        with open("data.json", "r") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        print("Kayıt bulunamadı.")
        return

    gelir = sum(item['amount'] for item in transactions if item['type'] == 'gelir')
    gider = sum(item['amount'] for item in transactions if item['type'] == 'gider')
    bakiye = gelir - gider

    print(f"Toplam Gelir: {gelir} TL")
    print(f"Toplam Gider: {gider} TL")
    print(f"Net Bakiye: {bakiye} TL")