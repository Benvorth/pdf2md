import pymupdf4llm
import requests
import os
import uuid
from fastapi import APIRouter

from api.requests import Pdf2MdRequest

router = APIRouter()


@router.post("/pdf2md/api/convert")
async def convert_pdf_url_to_md(rq: Pdf2MdRequest):
    return do_convert(rq)


def do_convert(rq: Pdf2MdRequest):

    # download pdf to local temp folder
    random_filename = f"{uuid.uuid4()}.pdf"
    tmp_filename_and_path = os.path.join("/tmp/dl/", random_filename)
    response = requests.get(rq.pdf_url)
    with open(tmp_filename_and_path, 'wb') as f:
        f.write(response.content)

    # do extraction
    md_texts = pymupdf4llm.to_markdown(tmp_filename_and_path, page_chunks=True)
    the_texts = [elem.get('text') for elem in md_texts]  # list of pages

    # clean up
    os.remove(tmp_filename_and_path)

    return " ".join(the_texts)

