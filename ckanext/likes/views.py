"""Views of the likes plugin.

All blueprints added to `__all__` are registered as blueprints inside Flask
app. If you have multiple blueprints, create them inside submodules of
`ckanext.likes.views` and re-export via `__all__`.

Example:
    ```python
    from .custom import custom_bp
    from .data import data_bp

    __all__ = ["custom_bp", "data_bp"]
    ```
"""

from __future__ import annotations

from flask import Blueprint

import ckan.plugins.toolkit as tk

__all__ = ["bp"]

bp = Blueprint("likes", __name__)


@bp.errorhandler(tk.ObjectNotFound)
def not_found_handler(error: tk.ObjectNotFound) -> tuple[str, int]:
    """Generic handler for ObjectNotFound exception."""
    return (
        tk.render(
            "error_document_template.html",
            {
                "code": 404,
                "content": f"Object not found: {error.message}",
                "name": "Not found",
            },
        ),
        404,
    )


@bp.errorhandler(tk.NotAuthorized)
def not_authorized_handler(error: tk.NotAuthorized) -> tuple[str, int]:
    """Generic handler for NotAuthorized exception."""
    return (
        tk.render(
            "error_document_template.html",
            {
                "code": 403,
                "content": error.message or "Not authorized to view this page",
                "name": "Not authorized",
            },
        ),
        403,
    )


@bp.route("/like/<type>/<id>", methods=["GET", "POST"])
def like(id: str, type: str):
    if tk.request.method == "POST":
        tk.get_action("likes_like_toggle")(
            {},
            {
                "id": id,
                "type": type,
            },
        )

    data = tk.get_action("likes_like_show")(
        {},
        {
            "id": id,
            "type": type,
        },
    )
    data["object_id"] = id
    data["object_type"] = type

    return tk.render("likes/snippets/widget.html", data)
