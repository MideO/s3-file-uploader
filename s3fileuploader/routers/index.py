from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="upload.html")


@router.post("/uploads", response_class=HTMLResponse)
async def upload_file(request: Request):
    # flash(request, 'File successfully uploaded')
    return templates.TemplateResponse(
        request=request,
        name="upload.html",
        context={"message": "File successfully uploaded"},
    )


@router.get("/uploads/<filename>", response_class=HTMLResponse)
async def download_file(_):
    return RedirectResponse(url="/")


@router.delete("/uploads/<filename>", response_class=HTMLResponse)
async def delete_file(_):
    return RedirectResponse(url="/")
