import json

def reset_data():
    with open("data.json", "w") as f:
        json.dump([], f)
    print("Tüm kayıtlar başarıyla sıfırlandı.")
