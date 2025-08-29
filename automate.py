import requests
import re
import json

def fetch_template_from_mediawiki(template_name="Infobox company"):
    """
    Fetch raw wikitext of a given template from English Wikipedia using MediaWiki API.
    """
    params = {
        "action": "query",
        "prop": "revisions",
        "rvprop": "content",
        "titles": f"Template:{template_name}",
        "format": "json",
        "formatversion": "2"
    }
    
    headers = {
        "User-Agent": "TemplateExtractorBot/1.0 (https://example.com; youremail@example.com)"
    }
    
    url = "https://en.wikipedia.org/w/api.php"
    response = requests.get(url, params=params, headers=headers)
    response.raise_for_status()

    data = response.json()

    try:
        wikitext = data["query"]["pages"][0]["revisions"][0]["content"]
        return wikitext
    except (KeyError, IndexError):
        return None



