import requests
from bs4 import BeautifulSoup

def get_problem_inputs(soup: BeautifulSoup) -> list:
    inputs = soup.find_all("div", class_="test-example-line")
    result = []
    
    for i in inputs:
        result.append(i.text)
        
    return result


def get_problem_content(url: str) -> list:
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    return get_problem_inputs(soup)
