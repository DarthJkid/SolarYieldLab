"""Bootstrap the project: create required directories."""
from pathlib import Path

from src.config.paths import ensure_directories, PROJECT_ROOT
from src.utils.logging_utils import get_logger
from src.config.settings import settings

def main() -> None:
    ensure_directories()
    logger = get_logger(__name__)
    logger.info("Project root: %s", PROJECT_ROOT)
    logger.info("Environment: %s", settings.environment)
    logger.info("Application name: %s", settings.app_name)
    logger.info("Bootstrap completed successfully.")


if __name__ == "__main__":
    main()
