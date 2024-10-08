from pydantic import BaseModel


class Pdf2MdRequest(BaseModel):
    pdf_url: str
