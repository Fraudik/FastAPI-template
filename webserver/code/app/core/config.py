from pydantic import BaseSettings


class Settings(BaseSettings):
    # CHANGE DB NAME (example.db is used only as template)
    # url naming: https://docs.sqlalchemy.org/en/20/core/engines.html#sqlite
    SQLALCHEMY_DATABASE_URI: str = "sqlite+aiosqlite:///app/storage/example.db"

    class Config:
        # case_sensitive: https://docs.pydantic.dev/usage/settings/#environment-variable-names
        case_sensitive = True


settings = Settings()
