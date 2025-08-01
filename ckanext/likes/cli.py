"""CLI commands for ckanext-likes.

Example:
    ```sh
    ckan likes --help
    ```
"""

from __future__ import annotations

import click

__all__ = ["likes"]


@click.group(short_help="likes CLI.")
def likes():
    pass
