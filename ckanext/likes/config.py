"""Config getters of likes plugin."""

from __future__ import annotations

import ckan.plugins.toolkit as tk

OPTION = "ckanext.likes.option.name"


def option() -> int:
    """Integer placerat tristique nisl."""
    return tk.config[OPTION]
