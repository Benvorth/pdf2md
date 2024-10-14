import pymupdf4llm
import requests
import os
import uuid
import json
from fastapi import APIRouter, HTTPException

from api.my_requests.Pdf2MdModel import Pdf2MdRequest

router = APIRouter()


@router.post("/pdf2md/api/convert")
async def convert_pdf_url_to_md(rq: Pdf2MdRequest):
    return do_convert(rq)


def do_convert(rq: Pdf2MdRequest):

    random_filename = f"{uuid.uuid4()}.pdf"
    tmp_dir = "/tmp/dl/"
    tmp_filename_and_path = os.path.join(tmp_dir, random_filename)

    try:
        # Ensure the directory exists
        os.makedirs(tmp_dir, exist_ok=True)

        # download pdf to local temp folder
        response = requests.get(rq.pdf_url)
        with open(tmp_filename_and_path, 'wb') as f:
            f.write(response.content)

        # do extraction
        md_texts = pymupdf4llm.to_markdown(tmp_filename_and_path, page_chunks=True)
        the_texts = [elem.get('text') for elem in md_texts]  # list of pages

        # clean up
        os.remove(tmp_filename_and_path)

        # FastAPI will automatically serialize Python data structures (like lists and dictionaries)
        # into JSON format and set the appropriate Content-Type.
        return the_texts
    except Exception as e:
        # Cleanup if an error occurs
        if os.path.exists(tmp_filename_and_path):
            os.remove(tmp_filename_and_path)
        raise HTTPException(status_code=500, detail=str(e))

