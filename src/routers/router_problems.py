from fastapi import APIRouter

from src.scrapper.get_problem import get_problem_content

router = APIRouter(prefix="/problems")

@router.get("/")
def get_problem(contest_id: str, id: str) -> list:
    result: list = get_problem_content(f"https://codeforces.com/contest/{contest_id}/problem/{id}")
    return result
