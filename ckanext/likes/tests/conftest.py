from __future__ import annotations

from typing import Any

import pytest


@pytest.fixture
def clean_db(reset_db: Any, migrate_db_for: Any):
    """Apply plugin migrations whenever CKAN DB is cleaned."""
    reset_db()
    migrate_db_for("likes")
