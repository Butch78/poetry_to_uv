from fastapi import APIRouter

router = APIRouter()


@router.post("/")
async def update_admin() -> dict:
    return {"message": "Admin getting schwifty"}
