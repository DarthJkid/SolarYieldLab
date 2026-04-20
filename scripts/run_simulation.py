"""Run PV yield simulation for one or more sites."""
from src.utils.logging_utils import get_logger

logger = get_logger(__name__)


def main() -> None:
    logger.info("Simulation runner started.")
    logger.info("No simulation logic has been connected yet.")
    logger.info("Next step: add NASA POWER and PVWatts clients.")


if __name__ == "__main__":
    main()
