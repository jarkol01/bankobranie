# Bankobranie — lokalna baza promocji bankowych

Lokalny scrape i strukturalna baza promocji z **https://www.bankobranie.pl**,
służąca do agregacji i wyboru optymalnej strategii „bankobrania" (zakładanie
kont osobistych/oszczędnościowych/firmowych, karty kredytowe/debetowe itd.).

## Struktura

```
.
├── README.md          # ten plik — opis struktury, pól i workflow
├── index.json         # MANIFEST: 1 wpis = 1 artykuł; szybki dedup + przegląd
├── _scrape-log.json   # historia przebiegów scrapowania
└── promocje/          # 1 plik .md = 1 artykuł/promocja (MD + YAML frontmatter)
    └── RRRR-MM-slug.md
```

- **1 plik = 1 artykuł.** Nazwa pliku = `RRRR-MM-slug` (z URL artykułu) — stabilna i sortowalna.
- Dane są **przetworzone, nie przepisane 1:1** — streszczamy i strukturyzujemy,
  zachowując wszystkie istotne fakty do podejmowania decyzji.

## Jak działa dedup / „czy już mamy ten artykuł"

`index.json` to spis treści. Klucz główny = **kanoniczny URL artykułu**.
Każdy wpis trzyma `content_hash` (skrót treści), więc wykrywamy też, czy
artykuł **zmienił się** od ostatniego scrapa (banki aktualizują promocje).

Przebieg „przeczesz ostatnie":
1. Pobierz listing strony głównej (Blogger: `search?max-results=N` lub paginacja
   przez `updated-max`). Idziemy w głąb przez kolejne strony.
2. Dla każdego URL: jest w `index.json`?
   - **nie** → nowy → pełny scrape + nowy plik + wpis w indeksie,
   - **tak, hash inny** → zaktualizowany → odśwież plik,
   - **tak, hash ten sam** → pomiń.
3. **Stop:** gdy na danej stronie zdecydowana większość promocji jest już
   nieaktywna (wygasłe terminy) — głębiej nie schodzimy.
4. Dopisz podsumowanie do `_scrape-log.json`.

## Legenda pól (frontmatter)

| Pole | Znaczenie |
|------|-----------|
| `id` | identyfikator = nazwa pliku bez `.md` |
| `url` | kanoniczny adres artykułu (klucz dedup) |
| `bank`, `produkt` | bank i nazwa produktu |
| `typ` | `konto_osobiste` \| `konto_oszczednosciowe` \| `konto_firmowe` \| `karta_kredytowa` \| `karta_debetowa` \| `inwestycje` \| `inne` |
| `status` | `aktywna` \| `wygasla` \| `nieznana` |
| `premia_total` | maksymalna kwota nagrody (zł) |
| `premia_components[]` | składowe nagrody: `nazwa`, `kwota`, `typ` (`gotowka`/`moneyback`/`oprocentowanie`/`rzecz`), `warunek` |
| `data_publikacji` | data publikacji artykułu |
| `data_koniec_przystapienia` | deadline na przystąpienie do promocji |
| `okres_warunkow_mies` | przez ile miesięcy trzeba spełniać warunki |
| `warunki` | strukturalnie: `wplyw_miesieczny_min`, `liczba_transakcji_min`, `transakcje_typ`, `transakcje_miejsce`, `logowanie_apka`, `inne[]` |
| `wyplata[]` | co i kiedy jest wypłacane |
| `oplaty` | `konto`, `karta`, `przelewy` + warunki zwolnienia |
| `ograniczenia` | `tylko_nowi_klienci`, `karencja_mies`, `wiek_min/max`, `inne[]` — KLUCZOWE dla łączenia promocji |
| `scraped_at`, `content_hash` | meta scrapowania |
| `tagi` | etykiety (z kategorii Bloggera + własne) |

## Statusy promocji

`status` wyliczamy względem `data_koniec_przystapienia` i daty scrapowania.
Promocje po terminie oznaczamy `wygasla`, ale **nie usuwamy** — przydają się do
historii i do oceny, które edycje wracają cyklicznie.
