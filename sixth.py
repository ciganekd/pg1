import sys
import requests
import re

def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []

    # Stáhne stránku
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"Chyba při stahování stránky: {response.status_code}")

    # změna na text
    content = response.text

    # všechny href
    hrefs = re.findall(r'<a\s+(?:[^>]*?\s+)?href="([^"]*)"', content)

    return hrefs

if __name__ == "__main__":
    try:
        url = sys.argv[1]
        odkazy = download_url_and_get_all_hrefs(url)
        print(odkazy)
    except Exception as e:
        print(f"Program skoncil chybou: {e}")
