from io import BytesIO
from unittest.mock import patch, MagicMock

import pytest
from fastapi import UploadFile

from ...src.routers import index


@pytest.mark.asyncio
@patch("s3fileuploader.src.routers.index.dependencies")
@patch("s3fileuploader.src.routers.index.templates.TemplateResponse")
async def test_upload_file(response, dependencies):
    dependencies.upload_task = MagicMock()
    dependencies.config.storage_path = ""
    request = MagicMock()
    file_content = BytesIO(b"Test file content")
    file_name = "test_upload.txt"
    file = UploadFile(filename=file_name, file=file_content)

    await index.upload_file(request, file)

    response.assert_called_with(
        request=request,
        name="upload.html",
        context={"message": "File successfully uploaded"},
    )
    dependencies.upload_task.apply_async.assert_called_with(
        (file_name, file_name, "test")
    )
