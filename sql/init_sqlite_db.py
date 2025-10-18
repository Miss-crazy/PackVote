from __future__ import annotations

import argparse
from pathlib import Path
import sqlite3


def _default_db_path() -> Path:
    return Path(__file__).resolve().parent / "packvote.sqlite"


def initialize_database(db_path: Path | None = None, schema_path: Path | None = None) -> Path:
    base_dir = Path(__file__).resolve().parent
    schema_file = schema_path or (base_dir / "schema.sql")
    target_db = Path(db_path) if db_path else _default_db_path()

    if not schema_file.exists():
        raise FileNotFoundError(f"Schema file not found at {schema_file}")

    target_db.parent.mkdir(parents=True, exist_ok=True)

    script = schema_file.read_text(encoding="utf-8")

    with sqlite3.connect(target_db) as conn:
        conn.executescript(script)

    return target_db


def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Initialize the PackVote SQLite database.")
    parser.add_argument(
        "--db-path",
        type=Path,
        default=None,
        help="Optional path for the SQLite database file (defaults to PackVote/sql/packvote.sqlite).",
    )
    parser.add_argument(
        "--schema",
        type=Path,
        default=None,
        help="Optional path to a schema SQL file (defaults to PackVote/sql/schema.sql).",
    )
    return parser.parse_args()


def main() -> None:
    args = _parse_args()
    db_path = initialize_database(db_path=args.db_path, schema_path=args.schema)
    print(f"Initialized SQLite database at {db_path}")


if __name__ == "__main__":
    main()
