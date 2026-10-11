#!/usr/bin/env python3
"""Scala promocje/*.idx.json -> index.json. Idempotentny.
Normalizacja: kanonizacja banku, premia_total 0->null, przeliczenie status
(wzgledem DZIS), przeliczenie content_hash, sort po deadline, aktualizacja _meta."""
import json, glob, re, sys
from collections import Counter

DZIS = "2026-10-11"

BANK_KANON = {
    "bank pekao": "Bank Pekao", "pekao": "Bank Pekao",
    "ing bank slaski": "ING Bank Śląski", "ing bank śląski": "ING Bank Śląski", "ing": "ING Bank Śląski",
    "bank millennium": "Bank Millennium", "millennium": "Bank Millennium",
    "pko bp": "PKO BP", "pko": "PKO BP",
    "mbank": "mBank",
    "alior bank": "Alior Bank", "alior": "Alior Bank",
    "erste bank": "Erste Bank", "erste": "Erste Bank",
    "bnp paribas": "BNP Paribas", "bnp": "BNP Paribas",
    "unicredit": "UniCredit",
    "velobank": "VeloBank",
    "nest bank": "Nest Bank", "nest": "Nest Bank",
    "bank pocztowy": "Bank Pocztowy", "pocztowy": "Bank Pocztowy",
    "citibank handlowy": "Citibank Handlowy", "citibank": "Citibank Handlowy", "citi": "Citibank Handlowy",
    "raiffeisen digital bank": "Raiffeisen Digital Bank", "raiffeisen": "Raiffeisen Digital Bank",
    "volkswagen bank": "Volkswagen Bank", "volkswagen": "Volkswagen Bank",
    "mastercard": "Mastercard",
}

def kanon_bank(b):
    if not b: return b
    return BANK_KANON.get(b.strip().lower(), b.strip())

def x(v):
    return "x" if v in (None, "", "null") else v

items = []
for f in sorted(glob.glob("promocje/*.idx.json")):
    it = json.load(open(f))
    it["bank"] = kanon_bank(it.get("bank"))
    # premia_total 0 -> null
    if it.get("premia_total") in (0, "0"):
        it["premia_total"] = None
    # status wzgledem dzis
    dk = it.get("data_koniec_przystapienia")
    if dk and it.get("status") != "wygasla":  # reczne "wygasla" (zastapiona/pula) wygrywa
        it["status"] = "wygasla" if dk < DZIS else "aktywna"
    elif not it.get("status"):
        it["status"] = "nieznana"
    # content_hash
    it["content_hash"] = "fp:%s|%s|%s" % (x(it.get("premia_total")), x(dk), x(it.get("okres_warunkow_mies")))
    # status -> frontmatter .md (zrodlo prawdy ma byc spojne z indeksem)
    md = it.get("plik") or f.replace(".idx.json", ".md")
    try:
        txt = open(md).read()
        txt2 = re.sub(r"^status: .*$", "status: " + it["status"], txt, count=1, flags=re.M)
        if txt2 != txt: open(md, "w").write(txt2)
    except FileNotFoundError:
        print("BRAK .md:", md)
    items.append(it)

# sort: aktywne wg najblizszego deadline, wygasle/nieznane na koncu
def sort_key(it):
    dk = it.get("data_koniec_przystapienia") or "9999-99-99"
    aktywna = 0 if it.get("status") == "aktywna" else 1
    return (aktywna, dk, it.get("id", ""))
items.sort(key=sort_key)

stat = Counter(i["status"] for i in items)
typ = Counter(i["typ"] for i in items)

idx = json.load(open("index.json"))
idx["_meta"].update({
    "ostatni_scrape": DZIS,
    "liczba_promocji": len(items),
    "wg_statusu": dict(stat),
    "wg_typu": dict(typ),
})
idx["promocje"] = items

json.dump(idx, open("index.json", "w"), ensure_ascii=False, indent=2)
print("Scalono %d promocji." % len(items))
print("Status:", dict(stat))
print("Typ:", dict(typ))
