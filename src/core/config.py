from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr
from fastapi.security import OAuth2PasswordBearer

class Settings(BaseSettings):
    POSTGRESQL_USER: SecretStr
    POSTGRESQL_PASSWORD: SecretStr
    POSTGRESQL_HOST: SecretStr
    POSTGRESQL_PORT: SecretStr
    POSTGRESQL_DATABASE: SecretStr
    SECRET_AUTH: SecretStr
    SECRET_RESET_VERIF: SecretStr
    
    model_config: SettingsConfigDict = SettingsConfigDict(
        env_file='.env',
        env_file_encoding='utf-8'
    )
    
config = Settings()