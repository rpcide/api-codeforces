from fastapi import APIRouter

from src.routers.router_problems import router as router_problems

router = APIRouter()

router.include_router(router_problems)
