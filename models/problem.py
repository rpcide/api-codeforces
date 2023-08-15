from typing import List
from pydantic import BaseModel

class Example(BaseModel):
    input: List[str]
    output: List[str]

class Problem(BaseModel):
    url: str
    name: str
    contest_id: str
    problem_id: str
    content: str
    input_specification: str
    output_specification: str
    examples: List[Example]
    tags: List[str]
