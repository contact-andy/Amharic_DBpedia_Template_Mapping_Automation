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


def extract_template_info(template_name):
    """
    Extract template name and its attributes from Wikipedia wikitext.
    Returns a dict in JSON-friendly format.
    """
    wikitext = fetch_template_from_mediawiki(template_name)
    if not wikitext:
        return {"error": "Template not found or empty content"}

    # Extract attribute names (parameters start with |)
    attributes = re.findall(r'\|\s*([\w\-]+)\s*=', wikitext)

    # Remove duplicates while preserving order
    seen = set()
    attributes = [x for x in attributes if not (x in seen or seen.add(x))]

    result = {
        "template_name": template_name,
        "attributes": attributes
    }

    return result



# Example usage
template_data = extract_template_info("Infobox company")
print(json.dumps(template_data, ensure_ascii=False, indent=2))
