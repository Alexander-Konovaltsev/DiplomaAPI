from fastapi import APIRouter
from fastapi.responses import RedirectResponse

router = APIRouter()

@router.get("/admin")
def admin_redirect():
    return RedirectResponse(url="/admin/")
