from datetime import datetime
from langchain_community.vectorstores.milvus import Milvus
from app.core.config import azureSettings, milvusSettings
from langchain_openai import AzureOpenAIEmbeddings, AzureChatOpenAI
from pymilvus import Connections, utility


class AzureCall:
    def __init__(self):
        azure_settings = azureSettings()
        self.azure_endpoint: str = azure_settings.azure_endpoint
        self.azure_embedding_model: str = azure_settings.azure_embedding_model
        self.azure_chat_model: str = azure_settings.azure_chat_model
        self.azure_apikey: str = azure_settings.azure_apikey

    def AzureEmbedding(self):
        try:
            print(f"[ {datetime.now()} ] utils.AzureEmbedding()")
            return AzureOpenAIEmbeddings(
                azure_endpoint=self.azure_endpoint,
                azure_deployment=self.azure_embedding_model,
                api_key=self.azure_apikey,
            )
        except Exception as e:
            raise Exception(f"getembedding failed: {e}")

    def AzureChat(self):
        try:
            print(f"[ {datetime.now()} ] utils.AzureChat()")
            return AzureChatOpenAI(
                azure_endpoint=self.azure_endpoint,
                azure_deployment=self.azure_chat_model,
                api_key=self.azure_apikey,
            )
        except Exception as e:
            raise Exception(f"getembedding failed: {e}")


class MilvusCall:
    def __init__(self, collection_name: str, drop_old: bool = False):
        self.collection_name: str = collection_name
        self.drop_old = drop_old

    def getVectorstore(self, embeddings: AzureOpenAIEmbeddings):
        try:
            print(f"[ {datetime.now()} ] utils.getVectorstore()")
            milvus_settings = milvusSettings()
            vectorstore = Milvus(
                embedding_function=embeddings,
                collection_name=self.collection_name,
                drop_old=self.drop_old,
                connection_args={"host": milvus_settings.milvus_host, "port": milvus_settings.milvus_port})
            return vectorstore
        except Exception as e:
            raise Exception(f"getVectorstore failed: {e}")

    def dropVectorstore(self):
        try:
            print(f"[ {datetime.now()} ] utils.dropVectorstore()")
            milvus_settings = milvusSettings()
            Connections.connect(
                alias="default",
                host=milvus_settings.milvus_host,
                port=milvus_settings.milvus_port)
            if utility.has_collection(self.collection_name):
                utility.drop_collection(self.collection_name)
                print(
                    f"[ {datetime.now()} ] utils.dropVectorstore({self.collection_name})")
            Connections.disconnect(alias="default")
        except Exception as e:
            if Connections is not None:
                Connections.disconnect(alias="default")
            raise Exception(f"dropVectorstore failed: {e}")
