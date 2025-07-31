from fastapi import APIRouter, Depends
from app.services import get_current_user

router=APIRouter()

@router.get("/public")
def public_route():
    return {"message": "This is a public route"}

@router.get("/protected")
def protected_route(user=Depends(get_current_user)):
    return {"message": f"Hello {user['sub']}, this is a protected route"}
