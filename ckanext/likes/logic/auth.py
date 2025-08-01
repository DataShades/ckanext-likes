from __future__ import annotations

from typing import Any

import ckan.plugins.toolkit as tk
from ckan import types


@tk.auth_allow_anonymous_access
def likes_like_toggle(context: types.Context, data_dict: dict[str, Any]):
    if not context["user"]:
        return {"success": True, "message": "Only authorized users can like things"}
    return {"success": True}


@tk.auth_allow_anonymous_access
def likes_like_show(context: types.Context, data_dict: dict[str, Any]):
    return {"success": True}
