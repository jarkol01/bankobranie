# CLAUDE.md

Wskazówki dla Claude Code przy pracy w tym repozytorium.

## Cel projektu

Lokalna, strukturalna baza promocji bankowych scrapowanych z **https://www.bankobranie.pl**.
Służy do agregacji danych i ułożenia **optymalnej, personalnej strategii „bankobrania"**:
zakładania kont (osobistych, oszczędnościowych, firmowych), lokat, kart kredytowych oraz
korzystania z programów poleceń — tak, by zmaksymalizować premie przy kontrolowanym wysiłku.

Decyzje użytkownika będą podejmowane **na podstawie tych danych**, więc priorytetem jest
**dokładność** (liczby, deadline'y, warunki, karencje) — przy zachowaniu zwięzłości
(dane przetworzone własnymi słowami, NIE kopiowane 1:1 ze źródła).

## Struktura repo

```
.
├── CLAUDE.md          # ten plik
├── README.md          # opis struktury, legenda pól, workflow (dla człowieka)
├── index.html         # APLIKACJA: interaktywny tracker planu (hostowany na GitHub Pages)
├── index.json         # MANIFEST: 1 wpis = 1 artykuł; szybki dedup + przegląd
├── _scrape-log.json   # historia przebiegów scrapowania
└── promocje/          # 1 promocja = 2 pliki:
    ├── <id>.md        #   pełne dane: YAML frontmatter + streszczenie
    └── <id>.idx.json  #   kompaktowy wpis do indeksu (sidecar)
```

- **`id` = nazwa pliku** (bez rozszerzenia), format `RRRR-MM-slug` (z daty i tematu artykułu) — stabilne, sortowalne.
- Źródłem prawdy dla danej promocji jest jej `.md`. `.idx.json` to wyciąg pól; `index.json` to scalone sidecary.

## ⚙️ Flow scrapowania — KLUCZOWE

**Model: koordynator + ekstraktorzy. Nie syntezuj wielu artykułów w jednym kontekście.**

Powód: wciągnięcie wielu promocji naraz do jednego kontekstu „zatruwa" go — mieszają się
kwoty, deadline'y i warunki między bankami, a błędy są trudne do wykrycia. Ekstrakcja
1-artykuł-na-agenta z czystym kontekstem jest wyraźnie dokładniejsza.

**Główny agent (koordynator):**
1. Pobiera listing przez WebFetch. Blogger: `https://www.bankobranie.pl/search?max-results=30&start=0`,
   kolejne strony przez `updated-max=<timestamp ostatniego wpisu>&start=30/60/90...` (link „Starsze posty").
2. Robi **dedup** względem `index.json` (klucz = `url`) i odsiewa:
   - duplikaty / starsze edycje tego, co już mamy (np. „edycja 7" zastępuje „edycję 5"),
   - wpisy niepromocyjne: przeglądy tygodnia, dzienniki („Moje zarabianie"), zbiorcze rankingi, loterie, „film"/duplikaty.
3. Rozdziela URL-e nowych/odrębnych promocji na **subagentów, batchami (~7–12 naraz)**.
4. Po batchu czyta krótkie raporty agentów, ocenia jakość, w razie wątpliwości ponawia.
5. Na końcu **scala sidecary** w `index.json` i dopisuje wpis do `_scrape-log.json`.

**Reguła STOP:** schodź na kolejne strony, dopóki przynoszą nowe aktywne promocje.
Zatrzymaj się, gdy strona jest w większości **wygasła / duplikatami** i nie pojawiają się nowe aktywne oferty.

**Subagent (ekstraktor) — 1 agent = 1 artykuł:**
- `subagent_type: general-purpose`, model **Sonnet** (mocny i szybki do ekstrakcji z jednej strony; Opus tylko gdy jakość zawodzi).
- Dostaje: dokładnie jeden URL, docelowy `id`, podpowiedź typu, pełny schemat pól.
- Sam pobiera artykuł (świeży kontekst), wyciąga fakty, **zapisuje bezpośrednio 2 pliki**: `promocje/<id>.md` i `promocje/<id>.idx.json`.
- **NIE dotyka `index.json`** (równoległy zapis = korupcja) — scalanie robi koordynator.
- Zwraca tylko 2–3 zdania podsumowania + ostrzeżenia o brakujących/niejednoznacznych danych.

## Schemat pliku `.md` (YAML frontmatter)

```yaml
id, url, bank, produkt
typ:    konto_osobiste | konto_oszczednosciowe | lokata | konto_firmowe |
        karta_kredytowa | karta_debetowa | moneyback | inwestycje | inne
status: aktywna | wygasla | nieznana
premia_total:   # maks. nagroda gotówkowa/moneyback w zł; null jeśli sama oprocentowanie
waluta: PLN
oprocentowanie: # tylko dla oszczędnościowych/lokat
  {stawka_proc, limit_kwoty, okres_mies, stawka_bez_warunku_proc}
premia_components:  # rozbicie nagrody
  - {nazwa, kwota, typ: gotowka|moneyback|oprocentowanie|rzecz, warunek}
data_publikacji, data_koniec_przystapienia, okres_warunkow_mies
warunki:
  {wplyw_miesieczny_min, liczba_transakcji_min, transakcje_typ,
   transakcje_miejsce: stacjonarne|online|dowolne|null, logowanie_apka, inne[]}
wyplata:        - {co, kiedy}
oplaty:         {konto, karta, przelewy}   # z warunkami zwolnienia
ograniczenia:   {tylko_nowi_klienci, karencja_mies, wiek_min, wiek_max, inne[]}
scraped_at, content_hash, tagi[]
```

Treść pod frontmatter: `## Streszczenie` (3–5 zdań własnymi słowami) ·
`## Na co uważać` (haczyki: karencja, online vs stacjonarne, ukryte opłaty, osobne deadline'y,
limity uczestników) · `## Źródło` (data pobrania + ew. rozwiązany URL przekierowania).

## Konwencje danych (normalizacja)

- **`content_hash`** = fingerprint zmiennych pól: `"fp:<premia_total>|<data_koniec_przystapienia>|<okres_warunkow_mies>"`
  (użyj `x` dla `null`). Służy do wykrywania zmian przy ponownym scrapowaniu tego samego URL.
- **`premia_total`**: `null` gdy promocja to samo oprocentowanie (brak premii gotówkowej). Nie zostawiaj `0`.
- **Nazwy banków kanoniczne**, z polskimi znakami: `Bank Pekao`, `ING Bank Śląski`, `Bank Millennium`, `PKO BP`, `mBank`, `Alior Bank`, `Erste Bank`, `BNP Paribas`, `UniCredit`, `VeloBank`, `Nest Bank`, `Bank Pocztowy`, `Citibank Handlowy`, `Raiffeisen Digital Bank`, `Volkswagen Bank`.
- **`status`**: wyliczany względem `data_koniec_przystapienia` i daty scrapowania.
  Wygasłych **nie usuwamy** — wiele edycji wraca cyklicznie (cenne dla przewidywania powrotów).
- **Daty**: zawsze `RRRR-MM-DD`. Gdy artykuł nie podaje dnia publikacji — przybliż do 1. dnia miesiąca i odnotuj.

## Specyfika źródła (bankobranie.pl)

- Silnik **Blogger**: paginacja `search?max-results=N&start=K&updated-max=...&by-date=false`.
- Część wpisów to **strony przekierowań** (np. `.../przekierowanie-N.html`) → rozwiń do realnego celu
  (artykuł docelowy lub link partnerski); w `url` zachowaj oryginalny adres z listingu, a cel dopisz w `## Źródło`.
- Etykiety/kategorie (do celowanego odświeżania): `aktywna promocja konta`, `aktywna promocja karty`,
  `aktualne promocje bankowe dla firm`, `aktywna promocja dla nieletnich`, oraz per-bank.

## Typowe zadania

- **„Przeczesz ostatnie / odśwież"** → wykonaj flow scrapowania (sekcja powyżej): listing → dedup → subagenci → scal → log.
  Jeśli URL jest już w `index.json` ale `content_hash` się zmienił → to aktualizacja (odśwież plik).
- **Scalanie sidecarów / normalizacja / przebudowa `index.json`** → skrypt `python3` iterujący po `promocje/*.idx.json`
  (kanonizacja banku, `premia_total` 0→null, przeliczenie `content_hash`, sort po deadline; aktualizacja `_meta`).
  Skrypt jest idempotentny — można puszczać po każdym batchu.
- **Analiza / strategia** → operuj na `index.json` (warstwa maszynowa); po szczegóły i haczyki sięgaj do `.md`.
  Profil użytkownika i wybrany plan są już ustalone — patrz sekcja „Strategia i research" oraz memory.
  Przy aktualizacji planu pamiętaj o przeliczeniu wpływu na `index.html` (obiekt `PLAN`) i `git push`.
- **Aktualizacja trackera / planu** → edytuj `PLAN` w `index.html`, commit + `git push` (Pages odświeża się samo).

## Aplikacja (tracker) + wdrożenie na GitHub Pages

`index.html` to samodzielna aplikacja webowa (jeden plik: HTML+CSS+JS inline, bez zależności,
działa też lokalnie z dwukliku). Zakładki: Pulpit · Harmonogram miesięczny · Produkty
(checklisty) · Spend plan · Zasady. Stan odhaczeń trzymany w **localStorage przeglądarki**
(czyli **per urządzenie** — nie synchronizuje się między telefonem a kompem; jest Eksport/Import JSON
do przenoszenia). Repo zawiera „czysty" tracker bez odhaczeń użytkownika.

**Wdrożenie (stan 2026-06-04):**
- Repo: **github.com/jarkol01/bankobranie** — PUBLICZNE (darmowy Pages wymaga publicznego repo).
- Hosting: **GitHub Pages**, źródło `main` / katalog główny (`/`). Adres: **https://jarkol01.github.io/bankobranie/**.
- Konto GitHub użytkownika: `jarkol01`; `gh` i `git` są dostępne i zalogowane (protokół SSH).
- **Aktualizacja:** edytuj plik → `git add -A && git commit && git push` → Pages przebuduje się sam (~1–2 min, pierwszy build dłużej; 404 zanim się postawi to normalne). Commit message kończ trailerem `Co-Authored-By: Claude Opus 4.8 (1M context) <noreply@anthropic.com>`.
- Dane planu są **wbudowane w `index.html`** (obiekt `PLAN`) — przy zmianie strategii edytuj ten obiekt, nie tylko bazę `promocje/`.

## Strategia i research (stan)

- **Strategia personalna jest już ułożona** i wdrożona w `index.html`. Profil użytkownika i wybrany plan
  zapisane w pamięci projektu (memory: `bankobranie-profil-uzytkownika`, `bankobranie-projekt`).
  W skrócie: użytkownik ma ≤26 lat (do lutego 2027), konto w mBanku (→ promocje mBank na konto osobiste zablokowane),
  swobodnie przepuszcza wpływy między bankami, wydaje ~3080 zł/mc (głównie ZEN, benefit ~1–2%), chce 1 kartę kredytową.
- **Ustalenia z researchu (przydatne na przyszłość):**
  - BLIK działa niezależnie w wielu bankach (brak konfliktu). Wpływy można „przepuszczać", o ile regulamin nie wymaga *„wynagrodzenia"*.
  - Transakcje do warunków rób zakupami, NIE doładowaniem ZEN/e-portfeli (wykluczone MCC).
  - Pekao: KONTO Przekorzystne ZAWSZE przed kartą kredytową (promocja konta wymaga braku produktów kredytowych „na dzień przystąpienia"; karta nie wymaga konta).
  - Karta kredytowa Pekao z Żubrem: limit **do 7000 zł bez dokumentów** (online); pusty BIK to główne ryzyko niższego limitu. Przewalutowanie po **tabeli banku ~3,9–4,3% spread** (nie kurs Mastercard) → słaba do FX, używać tylko gdzie wymagana (kaucja auta), resztę przez ZEN. Bankomat zagr. 7%/5%/3% — unikać.
- Research robić **osobnym subagentem** (Sonnet, WebSearch/WebFetch), nie zaśmiecać głównego kontekstu; prosić o rozróżnienie „potwierdzone w oficjalnym źródle vs praktyka" + URL-e.

## Środowisko

- `python3` dostępny (używany do scalania/normalizacji). Brak gwarancji `jq`/`node` — domyślnie `python3`.
- `git` + `gh` dostępne i zalogowane (`jarkol01`, SSH) — patrz wdrożenie powyżej.
- Dzisiejszą datę bierz z kontekstu sesji; statusy i terminy licz względem niej.
