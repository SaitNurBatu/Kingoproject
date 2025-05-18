import json
from datetime import datetime

def add_transaction():
    t_type = input("İşlem türü (gelir/gider): ").strip().lower()
    if t_type not in ['gelir', 'gider']:
        print("Geçersiz tür.")
        return
    try:
        amount = float(input("Tutar: "))
    except ValueError:
        print("Geçersiz tutar.")
        return
    desc = input("Açıklama: ")
    date = datetime.now().strftime("%Y-%m-%d")

    data = {
        "type": t_type,
        "amount": amount,
        "desc": desc,
        "date": date
    }

    try:
        with open("data.json", "r") as f:
            transactions = json.load(f)
    except FileNotFoundError:
        transactions = []

    transactions.append(data)
    with open("data.json", "w") as f:
        json.dump(transactions, f, indent=4)
    print("İşlem eklendi.")