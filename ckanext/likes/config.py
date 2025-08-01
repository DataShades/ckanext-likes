"""Config getters of likes plugin."""

from __future__ import annotations

import ckan.plugins.toolkit as tk

OPTION = "ckanext.likes.option.name"
MULTI = "ckanext.likes.multivalued.option"


def option() -> int:
    """Integer placerat tristique nisl."""
    return tk.config[OPTION]


def multivalued() -> list[str]:
    """Another option that will be parsed as a list of words."""
    return tk.config[MULTI]
