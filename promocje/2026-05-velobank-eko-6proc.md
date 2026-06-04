---
id: 2026-05-velobank-eko-6proc
url: https://www.bankobranie.pl/2026/05/velobank-elastyczne-konto-oszczednosciowe-edycja-7-2026.html
bank: VeloBank
produkt: VeloBank Elastyczne Konto Oszczędnościowe
typ: konto_oszczednosciowe
status: aktywna
premia_total: null
waluta: PLN
oprocentowanie:
  stawka_proc: 6
  limit_kwoty: 50000
  okres_mies: null
  okres_dni: 92
  stawka_bez_warunku_proc: 1
  oprocentowanie_progi:
    - segment: nowi_klienci
      progi:
        - zakres: "0–50 000 zł"
          stawka_proc: 6
        - zakres: "50 000–400 000 zł"
          stawka_proc: 4
        - zakres: "powyżej 400 000 zł"
          stawka_proc: 1
    - segment: obecni_klienci_nowe_srodki
      progi:
        - zakres: "0–200 000 zł"
          stawka_proc: 4.5
        - zakres: "200 000–400 000 zł"
          stawka_proc: 3
        - zakres: "powyżej 400 000 zł"
          stawka_proc: 1
premia_components: []
data_publikacji: 2026-05-21
data_koniec_przystapienia: "2026-06-12"
okres_warunkow_mies: null
warunki:
  wplyw_miesieczny_min: null
  liczba_transakcji_min: 5
  transakcje_typ: płatności bezgotówkowe kartą lub BLIK
  transakcje_miejsce: dowolne
  logowanie_apka: null
  inne:
    - Wymóg "nowych środków" – środki wpłacone po 18.05.2026 (data salda początkowego)
    - Bez spełnienia warunku 5 transakcji miesięcznie oprocentowanie spada do 1%
    - Limit łączny środków objętych promocją: 400 000 zł
wyplata:
  - co: Odsetki od konta oszczędnościowego
    kiedy: Kapitalizacja miesięczna
oplaty:
  konto: null
  karta: null
  przelewy: null
ograniczenia:
  tylko_nowi_klienci: false
  karencja_mies: null
  wiek_min: null
  wiek_max: null
  inne:
    - Nowi klienci (6%/4%): osoby, które nie posiadały produktów oszczędnościowych w VeloBanku od 31.12.2023 do 20.05.2026
    - Obecni klienci mogą skorzystać ze stawek 4,5%/3% na nowe środki (wpłacone po 18.05.2026)
    - Data salda początkowego: 18.05.2026 – liczy się nadwyżka nad saldem z tego dnia
    - Promocja trwa 92 dni od spełnienia warunków
    - Maksymalny limit środków objętych promocją: 400 000 zł
scraped_at: 2026-06-03
content_hash: "fp:x|2026-06-12|x"
tagi: [velobank, konto_oszczednosciowe, oprocentowanie]
---

## Streszczenie

VeloBank oferuje Elastyczne Konto Oszczędnościowe (edycja 7/2026) z oprocentowaniem do 6% w skali roku przez 92 dni dla nowych klientów (do 50 000 zł) oraz do 4,5% dla obecnych klientów na nowe środki (do 200 000 zł). Warunkiem uzyskania podwyższonego oprocentowania jest wykonanie minimum 5 płatności bezgotówkowych kartą lub BLIK miesięcznie – bez tego stawka spada do 1%. Promocja jest dostępna dla klientów, którzy przystąpią do 12.06.2026.

## Na co uważać

- **Warunek 5 transakcji miesięcznie:** bez spełnienia tego wymogu oprocentowanie spada drastycznie z 6% lub 4,5% do zaledwie 1% – fallback jest bardzo niski
- **Progi kwot dla nowych klientów:** stawka 6% obowiązuje tylko do 50 000 zł; nadwyżka 50 000–400 000 zł oprocentowana jest już 4%, a powyżej 400 000 zł – tylko 1%
- **Progi kwot dla obecnych klientów:** stawka 4,5% obowiązuje do 200 000 zł; nadwyżka 200 000–400 000 zł oprocentowana jest 3%, powyżej – 1%
- **Wymóg nowych środków:** liczy się wyłącznie nadwyżka nad saldem z 18.05.2026 – środki już posiadane na koncie nie kwalifikują się do wyższego oprocentowania
- **Deadline przystąpienia: 12.06.2026** – w dniu pobrania danych (2026-06-03) pozostało tylko 9 dni; należy działać niezwłocznie
- **Definicja nowego klienta jest restrykcyjna:** brak produktów oszczędnościowych w VeloBanku w okresie 31.12.2023–20.05.2026
- Promocja trwa 92 dni od spełnienia warunków, nie od przystąpienia – warto upewnić się, od kiedy liczony jest czas

## Źródło
Pobrano 2026-06-03 z bankobranie.pl
