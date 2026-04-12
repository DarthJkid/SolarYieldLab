"""Bootstrap the project: create required directories."""
import argparse


def main() -> None:
    from src.config.paths import DATA, RAW, INTERIM, PROCESSED, FEATURE_STORE, ARTIFACTS
    for d in [DATA, RAW, INTERIM, PROCESSED, FEATURE_STORE, ARTIFACTS]:
        d.mkdir(parents=True, exist_ok=True)
    print('Project directories initialised.')


if __name__ == "__main__":
    main()
