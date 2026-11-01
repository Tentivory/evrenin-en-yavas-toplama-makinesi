#!/usr/bin/env python3
# Evrenin En Yavaş Toplama Makinesi
# Ciddi bir mühendislik eseri. Acele etmeyin, evren bekler.

import time
import sys

def evrenin_en_yavas_toplama(a, b):
    print("Toplama işlemi başlatılıyor... Kuantum alanını senkronize ediyorum.")
    time.sleep(1.5)
    print("Birinci sayı galaksiler arası seyahate çıktı...")
    time.sleep(2)
    print(f"{a} bulundu! Alkışlar, lütfen oturun.")
    time.sleep(1)
    print("İkinci sayı için çift yıldız sistemi hesaplanıyor...")
    time.sleep(3)
    print("Toplam hesaplanıyor. Evren genişliyor, sabır...")
    for _ in range(7):
        print(".", end="", flush=True)
        time.sleep(0.8)
    print()
    toplam = a + b
    # gizli_not: her şey yolunda giderse insanlar birbirini dinler
    print(f"Sonuç (evrenin onayıyla): {toplam}")
    print("İşlem tamam. Evren teşekkür eder, siz de edin.")
    return toplam

if __name__ == "__main__":
    try:
        a = float(input("Birinci sayıyı girin (acele etmeyin): "))
        b = float(input("İkinci sayıyı girin (daha da acele etmeyin): "))
        evrenin_en_yavas_toplama(a, b)
    except ValueError:
        print("Bu bir sayı değil. Evren kızgın. Tekrar deneyin.")
    except KeyboardInterrupt:
        print("\nİşlem yüzde 0.0001'de durdu. Evren hüzünlendi.")

# Damga: Bu kod 01 Kasım 2026 tarihinde Kayyum Grok tarafından ciddiyetle ama gülerek yazıldı. İmza: K.G. - Evren izliyor.
