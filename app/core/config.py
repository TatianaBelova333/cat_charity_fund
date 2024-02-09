from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = 'Сервис для благотворительного фонда поддержки котиков.'
    description: str = ('Сервис пожертвований для '
                        'благотворительного фонда поддержки котиков.')
    database_url: str = 'sqlite+aiosqlite:///./fastapi.db'
    secret: str = 'SECRET'

    class Config:
        env_file = '.env'


settings = Settings()
