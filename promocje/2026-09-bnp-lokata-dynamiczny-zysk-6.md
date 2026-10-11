---
id: 2026-09-bnp-lokata-dynamiczny-zysk-6
url: https://www.bankobranie.pl/2026/09/bnp-paribas-lokata-dynamiczny-zysk.html
bank: BNP Paribas
produkt: Lokata Dynamiczny Zysk (4 miesiące, rosnące oprocentowanie)
typ: lokata
status: aktywna
premia_total: null
waluta: PLN
oprocentowanie:
  stawka_proc: 6
  limit_kwoty: 50000
  okres_mies: 4
  stawka_bez_warunku_proc: null
premia_components:
  - nazwa: Oprocentowanie progresywne 4%/5%/7%/8% w kolejnych miesiącach (średnio 6% p.a.)
    kwota: null
    typ: oprocentowanie
    warunek: lokata 1000–50000 zł założona w ciągu 1 miesiąca od otwarcia konta osobistego; brak umowy ramowej na konto osobiste/oszczędnościowe w BNP Paribas przez ostatnie 24 mies.
data_publikacji: 2026-09-14
data_koniec_przystapienia: null
okres_warunkow_mies: 4
warunki:
  wplyw_miesieczny_min: null
  liczba_transakcji_min: null
  transakcje_typ: null
  transakcje_miejsce: null
  logowanie_apka: null
  inne:
    - Wymagane konto osobiste w BNP Paribas; lokatę zakłada się w bankowości internetowej lub aplikacji w ciągu 1 miesiąca od otwarcia konta
    - Wpłata min. 1000 zł, max 50000 zł; jedna lokata promocyjna na klienta
wyplata:
  - co: Odsetki (kapitalizacja na koniec okresu lub przy zerwaniu)
    kiedy: Po zakończeniu 4-miesięcznego okresu lokaty
oplaty:
  konto: null
  karta: null
  przelewy: null
ograniczenia:
  tylko_nowi_klienci: true
  karencja_mies: 24
  wiek_min: null
  wiek_max: null
  inne:
    - Brak umowy ramowej na konto osobiste lub oszczędnościowe w BNP Paribas w ostatnich 24 miesiącach
    - Przy zerwaniu lokaty odsetki naliczane tylko za faktyczny okres
    - Środki objęte BFG do równowartości 100 000 EUR
scraped_at: 2026-10-11
content_hash: "fp:x|x|4"
tagi: [lokata, bnp_paribas, nowi_klienci, oprocentowanie_progresywne, wymaga_konta, 6proc_srednio]
---

## Streszczenie

BNP Paribas oferuje 4-miesięczną lokatę „Dynamiczny Zysk" z oprocentowaniem rosnącym: 4% w 1. miesiącu, 5% w 2., 7% w 3. i 8% w 4. (średnio ok. 6% rocznie; nagłówkowe „do 8%" dotyczy tylko ostatniego miesiąca). Lokatę na 1000–50000 zł można założyć wyłącznie po otwarciu konta osobistego (w ciągu miesiąca od jego otwarcia), w bankowości internetowej lub aplikacji. Oferta dla klientów bez konta osobistego/oszczędnościowego w banku przez ostatnie 24 miesiące. Autor podaje dostępność „do odwołania" (komentarz z 2026-09-17).

## Na co uważać

- **Brak daty końca:** artykuł pokazuje licznik bez daty; autor w komentarzu pisze „do odwołania" — `data_koniec_przystapienia` = null, status przyjęty jako aktywna.
- **Średnia 6%, nie 8%:** 8% tylko w 4. miesiącu; stawka `6` w polu to średnia.
- **Wymagane konto osobiste:** lokata tylko w ciągu 1 miesiąca od otwarcia konta (powiązane: `bnp-paribas-promocja-konta`, do 1100 zł).
- **Zerwanie:** odsetki tylko za faktyczny okres, więc zerwanie przed 4. miesiącem ucina najwyższe stawki.
- **Kapitalizacja** na koniec okresu/zerwanie (wg komentarza autora, nie regulaminu).
- **Brak danych:** opłaty, podatek, pełny regulamin (artykuł linkuje tylko tabelę oprocentowania i stronę promocji). Komentarz czytelnika o drugiej lokacie 4% do 50 tys. zł — niepotwierdzone.
- Brak programu poleceń; kod w formularzu to kod pracowniczy, niepotrzebny.

## Źródło

- Pobrano: 2026-10-11 z bankobranie.pl: https://www.bankobranie.pl/2026/09/bnp-paribas-lokata-dynamiczny-zysk.html
- Strona promocji: https://okazje-do-bankobrania.produktyfinansowe.pl/e/lead/1437/label=lokata?source=lt
- Data publikacji z nagłówka wpisu (2026-09-14).
