"""Launch the Streamlit app."""
import argparse


def main() -> None:
    import subprocess
    subprocess.run(['streamlit', 'run', 'app/Home.py'])


if __name__ == "__main__":
    main()
