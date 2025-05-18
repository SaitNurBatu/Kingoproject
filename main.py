from transaction import add_transaction
from report import show_report
from reset import reset_data

def main():
    while True:
        print("\n--- Kingo: Kişisel Gelir-Gider Takibi ---")
        print("1. Gelir/Gider Ekle")
        print("2. Rapor Göster")
        print("3. Raporu Sıfırla")
        print("4. Çıkış")
        choice = input("Seçiminiz: ")
        if choice == '1':
            add_transaction()
        elif choice == '2':
            show_report()
        elif choice == '3':
            reset_data()
        elif choice == '4':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim.")

if __name__ == "__main__":
    main()
