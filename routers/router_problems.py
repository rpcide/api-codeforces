from typing import Union
from fastapi import APIRouter, HTTPException, status
from models.problem import Problem

from scrapper.get_problem import get_problem_content

router = APIRouter(prefix="/problems")

@router.get("/", response_model=Union[Problem, None])
def get_problem(contest_id: str, id: str):
    result = get_problem_content(f"https://codeforces.com/contest/{contest_id}/problem/{id}")

    if result == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return result
