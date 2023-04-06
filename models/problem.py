from typing import List
from pydantic import BaseModel

class Problem(BaseModel):
    url: str
    name: str
    contest_id: str
    problem_id: str
    content: str
    input_specification: str
    output_specification: str
    input: List[str]
    output: List[str]
    tags: List[str]
