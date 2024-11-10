import shutil

from fastapi import APIRouter, Request, UploadFile, File
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from dependency_factory import dependencies


router = APIRouter()
templates = Jinja2Templates(directory="s3fileuploader/src/templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse(request=request, name="upload.html")


@router.post("/uploads", response_class=HTMLResponse)
async def upload_file(request: Request, file: UploadFile = File(...)) -> HTMLResponse:
    file_path = f"{dependencies.config.storage_path}{file.filename}"
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    dependencies.upload_task.apply_async((file_path, file.filename, "test"))

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
