from typing import List, Union
import requests
from bs4 import BeautifulSoup

from models.problem import Example, Problem


def format_values(value) -> List[str]:
    input_problem = str(value).replace("<pre>", "").replace(
        "</pre>", "").replace("<br/>", "\n")
    result = list(input_problem.split("\n"))
    result = list(map(lambda x: x.strip(), result))
    return list(filter(lambda val: len(val) > 0, result))


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


def get_examples(soup: BeautifulSoup) -> List[Example]:
    examples: List[Example] = []

    examples_container = soup.find("div", class_="sample-test")

    children = examples_container.findChildren("div", recursive=False)

    for i in range(0, len(children), 2):
        input_problem = children[i].find("pre")
        output_problem = children[i+1].find("pre")

        examples.append(
            Example(input=format_values(input_problem),
                    output=format_values(output_problem)
                    )
        )

    return examples


def get_problem_content(url: str) -> Union[Problem, None]:
    headers = {
        "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"
    }
    r = requests.get(url, headers=headers)
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
        examples=get_examples(soup),
        input_specification=get_input_specification(soup),
        output_specification=get_output_specification(soup),
        tags=get_tags(soup)
    )
