"""Tests for Something model."""

from __future__ import annotations

import pytest


# Always include `with_plugins` before `clean_db`
@pytest.mark.usefixtures("with_plugins", "clean_db")
class TestSomething:
    pass
