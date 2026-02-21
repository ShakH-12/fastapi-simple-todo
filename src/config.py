from pydantic_settings import BaseSettings
from typing import Union, List

class Settings(BaseSettings):
	app_name: str = "Simple FastAPI ToDo"
	debug: bool = True
	database_url: str = "sqlite+aiosqlite:///tasks.db"
	cors_origins: Union[List[str], str] = [
	    "http://localhost:7700",
	    "http://localhost:8080",
	    "http://127.0.0.1:7700",
	    "http://127.0.0.1:8080"
	]
	static_dir: str = "static"
	images_dir: str = "static/images"
	
	class Config:
		env_file = ".env"

settings = Settings()