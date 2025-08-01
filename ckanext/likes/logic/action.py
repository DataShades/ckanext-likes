from __future__ import annotations

from typing import Any

import sqlalchemy as sa

import ckan.plugins.toolkit as tk
from ckan import model, types

from ckanext.likes.model import Like

from . import schema


def _get_user_id(context: types.Context, data_dict: dict[str, Any]) -> str | None:
    if id := data_dict.get("user_id"):
        return id

    user = context.get("auth_user_obj")  # pyright: ignore[reportUnknownVariableType]
    if isinstance(user, model.User):
        return user.id

    if user := model.User.get(context["user"]):
        return user.id


@tk.side_effect_free
@tk.validate_action_data(schema.like_show)
def likes_like_show(context: types.Context, data_dict: dict[str, Any]):
    """Show like-stats of the object."""
    stmt = Like.by_object(data_dict["id"], data_dict["type"])
    count = model.Session.scalar(stmt.with_only_columns(sa.func.count()))

    if user_id := _get_user_id(context, data_dict):
        liked = Like.exists(data_dict["id"], data_dict["type"], user_id)
    else:
        liked = False

    return {"count": count, "liked": liked}


@tk.validate_action_data(schema.like_show)
def likes_like_toggle(context: types.Context, data_dict: dict[str, Any]):
    """Toggle liked state of the object."""
    user_id = _get_user_id(context, data_dict)
    if not user_id or Like.unlike(data_dict["id"], data_dict["type"], user_id):
        liked = False

    else:
        obj = Like(
            object_id=data_dict["id"], object_type=data_dict["type"], user_id=user_id
        )
        model.Session.add(obj)
        liked = True

    if not context.get("defer_commit"):
        model.Session.commit()

    return {"liked": liked}
