from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):

    model_config = SettingsConfigDict(env_file=".env",extra="ignore")

class SecurityVariables(Settings):

    OPENAI_API_KEY: str
    LANGCHAIN_API_KEY: str