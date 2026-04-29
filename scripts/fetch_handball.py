"""
fetch_handball.py
Ruft Spielplan und Tabelle für mehrere Mannschaften des TuS Esingen ab
und speichert sie als JSON.
"""

import requests, json, os
from datetime import datetime

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; TuSEsingenBot/1.0)",
    "Accept": "application/json",
    "Referer": "https://www.handball.net/"
}

BASE = "https://api.handball.net"

# Mannschafts-Konfiguration
TEAMS = [
    {
        "ordner": "1-herren",
        "name": "1. Herren",
        "liga": "Männer Oberliga Hamburg",
        "team_id": "handball4all.hamburg.1260656",
        "liga_id": "handball4all.hamburg.m-ol-100_hhv",
    },
    {
        "ordner": "1-damen",
        "name": "1. Damen",
        "liga": "Frauen Landesliga Gruppe 1",
        "team_id": "handball4all.hamburg.1331421",
        "liga_id": "handball4all.hamburg.f-ll-221_hhv",
    },
]


def fetch_spielplan(team_id):
    url = f"{BASE}/teams/{team_id}/schedule"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def fetch_tabelle(liga_id):
    url = f"{BASE}/tournaments/{liga_id}/table"
    r = requests.get(url, headers=HEADERS, timeout=30)
    r.raise_for_status()
    return r.json()


def normalize_spiele(raw, eigene_team_id):
    spiele = []
    for s in raw.get("data", []):
        spiele.append(s)
    return spiele


def normalize_tabelle(raw):
    return raw.get("data", [])


def verarbeite_team(team):
    print(f"\n=== {team['name']} ===")
    ordner = f"data/{team['ordner']}"
    os.makedirs(ordner, exist_ok=True)
    updated = datetime.now().strftime("%d.%m.%Y")

    # Spielplan
    try:
        raw_sp = fetch_spielplan(team["team_id"])
        spiele = normalize_spiele(raw_sp, team["team_id"])
        output = {
            "aktualisiert": updated,
            "team": team["name"],
            "spiele": spiele,
        }
        with open(f"{ordner}/spielplan.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"  spielplan.json geschrieben ({len(spiele)} Spiele)")
    except Exception as e:
        print(f"  FEHLER Spielplan: {e}")

    # Tabelle
    try:
        raw_tab = fetch_tabelle(team["liga_id"])
        zeilen = normalize_tabelle(raw_tab)
        output = {
            "aktualisiert": updated,
            "liga": team["liga"],
            "tabelle": zeilen,
        }
        with open(f"{ordner}/tabelle.json", "w", encoding="utf-8") as f:
            json.dump(output, f, ensure_ascii=False, indent=2)
        print(f"  tabelle.json geschrieben ({len(zeilen)} Teams)")
    except Exception as e:
        print(f"  FEHLER Tabelle: {e}")


def main():
    print(f"Start: {datetime.now().isoformat()}")
    for team in TEAMS:
        verarbeite_team(team)
    print("\nFertig!")


if __name__ == "__main__":
    main()
