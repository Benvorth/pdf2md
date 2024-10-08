from fastapi import APIRouter

router = APIRouter()


@router.get('/pdf2md/api/common/alive/')
async def read_root():
    return {"status": 200, "message": "pdf2md service alive!"}

