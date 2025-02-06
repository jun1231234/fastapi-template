from datetime import datetime
import logging
from fastapi import APIRouter, HTTPException
from langchain_core.documents.base import Document
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from fastapi import requests, File, UploadFile
from fastapi.responses import JSONResponse
from app.utils import AzureCall, MilvusCall

# 로그 설정
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
)
logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/chatTest")
async def chatTest():
    try:
        logger.debug(f"[ {datetime.now()} ] : techatTestt")
        print(f"[ {datetime.now()} ] : techatTestt")
        return "chatTest"

    except Exception as e:
        logger.debug(f"[ {datetime.now()} ] : chatTest Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/uploadFile")
async def uploadFile(file: UploadFile = File(...)):
    try:
        logger.debug(f"[ {datetime.now()} ] : uploadFile")
        file_content = await file.read()
        response = JSONResponse(content={
            "filename": file.filename,
            "content_type": file.content_type,
            "file_size": len(file_content)
        })
        return response

    except Exception as e:
        logger.debug(f"[ {datetime.now()} ] : uploadFile Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/Quokka")
async def Quokka():
    try:
        logger.debug(f"[ {datetime.now()} ] : Quokka")
        return "Quokka"

    except Exception as e:
        logger.debug(f"[ {datetime.now()} ] : Quokka Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/QuokkaVectorstore")
async def callQuQuokkaVectorstoreokka():
    try:
        logger.debug(f"[ {datetime.now()} ] : QuokkaVectorstore")
        return "QuokkaVectorstore"

    except Exception as e:
        logger.debug(f"[ {datetime.now()} ] : QuokkaVectorstore Error: {e}")
        raise HTTPException(status_code=400, detail=str(e))


# @router.post("/embedding")
# async def embedding(collection_name: str):
#     try:
#         print(f"[ {datetime.now()} ] : chat.embedding()")
#         docs: list[Document] = []
#         auzre = AzureCall()
#         milvus = MilvusCall(collection_name)
#         milvus.dropVectorstore()
#         load_docs = TextLoader('./app/test/test.txt').load()
#         embedding_docs = RecursiveCharacterTextSplitter(
#             chunk_size=300, chunk_overlap=15).split_documents(load_docs)
#         for i, value in enumerate(embedding_docs):
#             docs.append(Document(
#                 page_content=value.page_content,
#                 metadata={"page": i})
#             )
#         vectorstore = milvus.getVectorstore(auzre.AzureEmbedding())
#         vectorstore = vectorstore.from_documents(
#             documents=docs,
#             embedding=auzre.AzureEmbedding()
#         )
#         return True
#     except Exception as e:
#         raise Exception(f"chat.embedding failed: {e}")
