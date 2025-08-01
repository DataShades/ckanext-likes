"""Template helpers of the likes plugin.

All non-private functions defined here are registered inside `tk.h` collection.
"""

from __future__ import annotations


def likes_hello() -> str:
    """Greet the user.

    Returns:
        greeting with the plugin name.
    """
    return "Hello, likes!"
