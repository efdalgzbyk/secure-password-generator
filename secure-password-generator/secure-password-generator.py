import random
import string

def sifre_uret(uzunluk=12, buyuk=True, kucuk=True, rakam=True, sembol=True):
    karakter_havuzu = ''
    
    if buyuk:
        karakter_havuzu += string.ascii_uppercase
    if kucuk:
        karakter_havuzu += string.ascii_lowercase
    if rakam:
        karakter_havuzu += string.digits
    if sembol:
        karakter_havuzu += string.punctuation

    if not karakter_havuzu:
        raise ValueError("En az bir karakter türü seçmelisiniz.")

    return ''.join(random.choice(karakter_havuzu) for _ in range(uzunluk))


def evet_hayir_sorusu(soru):
    while True:
        cevap = input(soru + " (e/h): ").lower()
        if cevap in ['e', 'h']:
            return cevap == 'e'
        print("Lütfen sadece 'e' veya 'h' giriniz.")


def main():
    print("🔐 Güçlü Şifre Oluşturucu")
    
    try:
        uzunluk = int(input("Şifre uzunluğunu girin (örnek: 12): "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        return

    buyuk = evet_hayir_sorusu("Büyük harf kullanılsın mı?")
    kucuk = evet_hayir_sorusu("Küçük harf kullanılsın mı?")
    rakam = evet_hayir_sorusu("Rakam kullanılsın mı?")
    sembol = evet_hayir_sorusu("Sembol kullanılsın mı?")

    try:
        sifre = sifre_uret(uzunluk, buyuk, kucuk, rakam, sembol)
        print(f"\n✅ Oluşturulan Şifre: {sifre}")
    except ValueError as e:
        print(f"Hata: {e}")

if __name__ == "__main__":
    main()
