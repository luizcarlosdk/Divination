from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    config = SettingsConfigDict(env_file=".env")


class SecurityVariables(Settings):

    api_openai_key: str
    api_langchain_key: str

    @property
    openai_key(self):
        return api_openai_key
    
    @property
    langchain_key(self):
        return api_langchain_key