from fastapi import APIRouter

router = APIRouter(prefix="/problems")

@router.get("/{id}")
def get_problem(id: str):
    return id
