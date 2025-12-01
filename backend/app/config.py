"""
Application Configuration
Uses Pydantic BaseSettings for environment variable management
"""
from pathlib import Path
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Database
    database_url: str = "postgresql://user:pass@localhost:5432/vitalpath"
    
    # Paths
    data_dir: Path = Path("/data")
    bundle_output_dir: Path = Path("/data/compiled")
    
    # API
    api_prefix: str = "/api/v1"
    debug: bool = False
    
    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = Settings()
