from functools import lru_cache
from pydantic_settings import BaseSettings


class MilvusSettings(BaseSettings):
    milvus_host: str = 'MILVUS_HOST'
    milvus_port: int = 'MILVUS_PORT'
    milvus_collection: str = 'MILVUS_COLLECTION'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        # extra 필드를 무시하거나 허용하지 않음으로써 다른 입력을 차단할 수 있습니다.
        extra = "ignore"


class AzureSettings(BaseSettings):
    azure_endpoint: str = 'AZURE_ENDPOINT'
    azure_apikey: str = 'AZURE_APIKEY'
    azure_apiversion: str = 'AZURE_APIVERSION'
    azure_chat_model: str = 'AZURE_CHAT_MODEL'
    azure_embedding_model: str = 'AZURE_EMBEDDING_MODEL'

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
        # extra 필드를 무시하거나 허용하지 않음으로써 다른 입력을 차단할 수 있습니다.
        extra = "ignore"


@lru_cache
def milvusSettings() -> MilvusSettings:
    return MilvusSettings()


@lru_cache
def azureSettings() -> AzureSettings:
    return AzureSettings()
