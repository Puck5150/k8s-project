import pathlib
import sys

import yaml


def main() -> int:
    errors = 0

    for path in pathlib.Path("k8s").glob("*.yaml"):
        try:
            with path.open() as file:
                list(yaml.safe_load_all(file))
            print(f"OK: {path}")
        except Exception as error:
            errors += 1
            print(f"ERROR: {path}: {error}")

    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())