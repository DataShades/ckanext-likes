from __future__ import annotations

from ckan import types
from ckan.logic.schema import validator_args


@validator_args
def like_toggle(
    unicode_only: types.Validator,
    not_empty: types.Validator,
    ignore_empty: types.Validator,
    ignore_not_sysadmin: types.Validator,
) -> types.Schema:
    return {
        "id": [not_empty, unicode_only],
        "type": [not_empty, unicode_only],
        "user_id": [ignore_not_sysadmin, ignore_empty, unicode_only],
    }


@validator_args
def like_show(
    unicode_only: types.Validator,
    not_empty: types.Validator,
    ignore_empty: types.Validator,
    ignore_not_sysadmin: types.Validator,
) -> types.Schema:
    return {
        "id": [not_empty, unicode_only],
        "type": [not_empty, unicode_only],
        "user_id": [ignore_not_sysadmin, ignore_empty, unicode_only],
    }
