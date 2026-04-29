"""
fetch_handball.py
Ruft Spielplan und Tabelle der 1. Herren von handball.net ab
und speichert sie als JSON in data/
"""

import requests, json, os
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; TuSEsingenBot/1.0)",
    "Accept": "application/json",
    "Referer": "https://www.handball.net/"
}

BASE = "https://api.handball.net"

def fetch_spielplan():
    url = f"{BASE}/mannschaften/handball4all.hamburg.1260656/spiele"
    params = {"dateFrom": "2025-07-01", "dateTo": "2026-06-30"}
    try:
        r = requests.get(url, headers=HEADERS, params=params, timeout=15)
        r.raise_for_status()
        data = r.json()
        print(f"Spielplan: {len(data.get('games', []))} Spiele abgerufen")
        return data
    except Exception as e:
        print(f"FEHLER Spielplan: {e}")
        return None

def fetch_tabelle():
    url = f"{BASE}/ligen/handball4all.hamburg.m-ol-100_hhv/tabelle"
    try:
        r = requests.get(url, headers=HEADERS, timeout=15)
        r.raise_for_status()
        data = r.json()
        print(f"Tabelle: {len(data.get('rows', []))} Mannschaften abgerufen")
        return data
    except Exception as e:
        print(f"FEHLER Tabelle: {e}")
        return None

def normalize_spielplan(raw):
    games = raw.get("games", raw.get("data", []))
    result = []
    for g in games:
        result.append({
            "liga":     g.get("competition", {}).get("name", ""),
            "datum":    g.get("scheduledAt", ""),
            "heim":     g.get("home", {}).get("name", ""),
            "gast":     g.get("guest", {}).get("name", ""),
            "heimLogo": g.get("home", {}).get("logoUrl", ""),
            "gastLogo": g.get("guest", {}).get("logoUrl", ""),
            "toreHeim": g.get("result", {}).get("home"),
            "toreGast": g.get("result", {}).get("guest"),
            "halle":    g.get("gym", {}).get("name", ""),
            "status":   g.get("status", ""),
            "hinweis":  g.get("note", "")
        })
    return result

def normalize_tabelle(raw):
    rows = raw.get("rows", raw.get("data", []))
    result = []
    for row in rows:
        result.append({
            "platz":    row.get("rank", 0),
            "verein":   row.get("team", {}).get("name", ""),
            "logo":     row.get("team", {}).get("logoUrl", ""),
            "spiele":   row.get("games", 0),
            "siege":    row.get("wins", 0),
            "niederl":  row.get("losses", 0),
            "diff":     row.get("goalDiff", 0),
            "punkte":   row.get("points", 0),
            "highlight": row.get("team", {}).get("name", "") == "TuS Esingen"
        })
    return result

def main():
    os.makedirs("data/1-herren", exist_ok=True)
    updated = datetime.now().strftime("%d.%m.%Y %H:%M")

    raw_sp = fetch_spielplan()
    if raw_sp is not None:
        spiele = normalize_spielplan(raw_sp)
        output = {"aktualisiert": updated, "mannschaft": "1. Herren", "spiele": spiele}
        with open("data/1-herren/spielplan.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"spielplan.json geschrieben ({len(spiele)} Spiele)")

    raw_tab = fetch_tabelle()
    if raw_tab is not None:
        zeilen = normalize_tabelle(raw_tab)
        output = {"aktualisiert": updated, "liga": "Männer Oberliga Hamburg", "tabelle": zeilen}
        with open("data/1-herren/tabelle.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"tabelle.json geschrieben ({len(zeilen)} Teams)")

    print("Fertig!")

if __name__ == "__main__":
    main()
