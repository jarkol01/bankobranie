---
id: 2026-09-velobank-velolokata-6proc-ed9
url: https://www.bankobranie.pl/2026/09/velolokata-dla-aktywnych-edycja-9-2027.html
bank: VeloBank
produkt: VeloLokata dla Aktywnych (edycja 9/2026)
typ: lokata
status: aktywna
premia_total: null
waluta: PLN
oprocentowanie:
  stawka_proc: 6.0
  limit_kwoty: 50000
  okres_mies: 6
  stawka_bez_warunku_proc: 2.0
premia_components: []
data_publikacji: 2026-09-17
data_koniec_przystapienia: 2026-11-04
okres_warunkow_mies: 6
warunki:
  wplyw_miesieczny_min: 2000
  liczba_transakcji_min: null
  transakcje_typ: null
  transakcje_miejsce: null
  logowanie_apka: null
  inne:
    - Wpływy co najmniej 2000 zł w każdym pełnym miesiącu kalendarzowym trwania lokaty (dowolny przelew przychodzący, bez wymogu utrzymania środków)
    - Wpływ musi pochodzić spoza VeloBanku (przelewy z innych kont detalicznych VeloBanku nie liczą się; z innych banków tak)
    - Wymagane zgody marketingowe (telekomunikacyjne/automatyczne, handlowe drogą elektroniczną, marketing/prawnie uzasadniony interes) i brak sprzeciwu na marketing bezpośredni, utrzymane do końca lokaty
    - Konto osobiste w VeloBanku musi być otwarte do końca lokaty
    - Zakładanie przez bankowość internetową lub aplikację
wyplata:
  - co: odsetki wg stawki 6% rocznie
    kiedy: po zakończeniu okresu lokaty (6 miesięcy); częstotliwość wypłaty nie podana w artykule
oplaty:
  konto: null
  karta: null
  przelewy: null
ograniczenia:
  tylko_nowi_klienci: true
  karencja_mies: null
  wiek_min: 18
  wiek_max: null
  inne:
    - Brak produktów oszczędnościowych w VeloBanku (konta oszczędnościowe, lokaty, IKE) w okresie 31.12.2023 – 16.09.2026
    - Jeden klient może założyć tylko jedną lokatę promocyjną
    - Minimalna kwota lokaty: 1000 zł
    - Zerwanie lokaty przed terminem: zwrot kapitału bez odsetek
    - Niespełnienie warunku w którymkolwiek miesiącu: oprocentowanie 2% za cały okres
scraped_at: "2026-10-11"
content_hash: "fp:x|2026-11-04|6"
tagi:
  - lokata
  - velobank
  - velolokata-dla-aktywnych
  - 6proc
  - edycja-9
---

## Streszczenie

VeloBank w edycji 9/2026 oferuje 6-miesięczną VeloLokatę dla Aktywnych z oprocentowaniem 6% rocznie na kwotę 1000–50 000 zł, zakładaną online lub w aplikacji. Pełna stawka wymaga wpływów min. 2000 zł miesięcznie na konto osobiste w VeloBanku w każdym pełnym miesiącu trwania lokaty, z zewnętrznych banków. Oferta dla osób bez produktów oszczędnościowych w VeloBanku od 31.12.2023 do 16.09.2026. Przystąpienie do 4 listopada 2026; jedna lokata promocyjna na klienta.

## Na co uważać

- **Jeden słaby miesiąc = 2% za cały okres**, nie tylko za ten miesiąc. Liczą się pełne miesiące kalendarzowe (np. lokata od 2.10.2026 do 2.04.2027 wymaga wpływów w XI–III, czyli 5 miesiącach); `okres_warunkow_mies: 6` to długość lokaty, nie liczba miesięcy z wymogiem.
- Przelewy z innych kont detalicznych VeloBanku nie liczą się; z kont w innych bankach tak.
- Zgody marketingowe i konto osobiste muszą trwać do końca lokaty.
- Zerwanie lokaty = utrata wszystkich odsetek.
- Artykuł nie precyzuje, czy to wyłącznie nowi klienci (tylko reguła braku produktów oszczędnościowych); `tylko_nowi_klienci: true` jako przybliżenie. Wiek 18+ (osoby pełnoletnie).
- Brak w artykule: częstotliwość wypłaty odsetek, opłaty (odsyłacz do tabeli opłat). Slug URL mówi „2027", treść „2026" — nieścisłość w źródle.
- Powiązane: 50 zł za konto z kodem polecającym (osobny wpis).

## Źródło

Pobrano 2026-10-11 z: https://www.bankobranie.pl/2026/09/velolokata-dla-aktywnych-edycja-9-2027.html
Brak przekierowania. Regulamin ed. 9/2026 i tabele: linki Google Drive w artykule; strona promocji: https://bankobranie.org/konto_velobank_velolokata
