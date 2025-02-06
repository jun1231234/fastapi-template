from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from app.api.main import api_router

prefix = "/backend"


def create_app():
    app = FastAPI(
        openapi_url=f"{prefix}/openapi.json",
        # Open API 코드 확인 테마 적용
        swagger_ui_parameters={"syntaxHighlight.theme": "obsidian"}
    )

    # CORS 이슈 회피를 위한 미들웨어 추가
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    # Route 정의
    app.include_router(api_router, prefix=f"{prefix}")

    return app


app = create_app()


@app.get("/")
async def healthcheck():
    return {"ok": True}
