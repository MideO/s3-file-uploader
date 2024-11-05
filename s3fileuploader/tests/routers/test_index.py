from io import BytesIO
from unittest.mock import patch, MagicMock

import pytest
from fastapi import UploadFile

from ...src.routers import index


@pytest.mark.asyncio
@patch("s3fileuploader.src.routers.index.dependencies.s3_service")
@patch("s3fileuploader.src.routers.index.templates.TemplateResponse")
async def test_upload_file(response, s3_service):
    s3_service.upload_file = MagicMock()
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
    s3_service().upload_file.assert_called_with(
        content=file_content, filename=file_name, bucket="test"
    )
