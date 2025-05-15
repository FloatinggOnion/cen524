import requests
from bs4 import BeautifulSoup

url = "https://developers.korapay.com/"

response = requests.get(url)
soup = BeautifulSoup(response.content, 'lxml')

# Example: extract headers and paragraphs
content = {
    "title": soup.find("h1").get_text(strip=True),
    "sections": []
}

for section in soup.find_all("section"):
    heading = section.find(["h2", "h3"])
    paragraphs = section.find_all("p")
    code_blocks = section.find_all("code")
    
    content["sections"].append({
        "heading": heading.get_text(strip=True) if heading else None,
        "text": [p.get_text(strip=True) for p in paragraphs],
        "code": [code.get_text(strip=True) for code in code_blocks]
    })

print(content)
