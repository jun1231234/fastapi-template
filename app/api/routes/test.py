from datetime import datetime
from fastapi import APIRouter, HTTPException
import logging

# logging 처리
logger = logging.getLogger("test")
logger.setLevel(logging.DEBUG)

router = APIRouter()


@router.get("/test")
async def test():
    try:
        logger.debug(f"[ {datetime.now()} ] : test")
        return "test"

    except Exception as e:
        logger.debug(f"[ {datetime.now()} ] : test Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))
