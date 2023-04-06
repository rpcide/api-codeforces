from typing import List, Union
import requests
from bs4 import BeautifulSoup

from models.problem import Problem

def get_problem_inputs(soup: BeautifulSoup) -> List[str]:
    inputs = soup.find_all("div", class_="test-example-line")
    result = []
    
    for i in inputs:
        result.append(i.text)
        
    return result

def get_problem_outputs(soup: BeautifulSoup) -> List[str]:
    output_container = soup.find("div", class_="output")
    out = output_container.find("pre").text
    out_splited = list(out.split("\n"))
    result = list(filter(lambda x : len(x)>0, out_splited))
    return result


def get_title(soup: BeautifulSoup) -> str:
    title = soup.find("div", class_="title")
    return title.text


def get_content(soup: BeautifulSoup) -> str:
    problem_content = soup.find("div", class_="problem-statement")
    content = problem_content.select(".problem-statement > div")
    return content[1].text


def get_input_specification(soup: BeautifulSoup) -> str:
    content = soup.find("div", class_="input-specification")
    return content.text


def get_output_specification(soup: BeautifulSoup) -> str:
    content = soup.find("div", class_="output-specification")
    return content.text


def get_tags(soup: BeautifulSoup) -> List[str]:
    tags_content = soup.find_all("span", class_="tag-box")
    result = []
    
    for i in tags_content:
        result.append(i.text.strip())
        
    return result


def get_problem_content(url: str) -> Union[Problem, None]:
    r = requests.get(url)
    html = r.content
    soup = BeautifulSoup(html, "html.parser")
    url_splited = r.url.split("/")

    if r.status_code != 200 or len(url_splited) <= 4:
        return None

    return Problem(
        contest_id=url_splited[4],
        problem_id=url_splited[6],
        url=r.url,
        name=get_title(soup),
        content=get_content(soup),
        input=get_problem_inputs(soup), 
        output=get_problem_outputs(soup),
        input_specification=get_input_specification(soup),
        output_specification=get_output_specification(soup),
        tags=get_tags(soup)
    )
