from __future__ import annotations

from datetime import datetime
from typing import Any

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, backref, relationship
from typing_extensions import override

from ckan import model
from ckan.lib.dictization import table_dictize

from .base import Base, now


class Like(Base):  # pyright: ignore[reportUntypedBaseClass]
    __table__ = sa.Table(
        "likes_like",
        Base.metadata,
        sa.Column("object_id", sa.Text(), primary_key=True),
        sa.Column("object_type", sa.Text(), primary_key=True),
        sa.Column(
            "user_id",
            sa.Text(),
            sa.ForeignKey("user.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("created_at", sa.DateTime(True), default=now),
    )

    # typed models. You'll use it - you'll love it.
    object_id: Mapped[str]
    object_type: Mapped[str]
    user_id: Mapped[str]

    created_at: Mapped[datetime]

    user: Mapped[model.User | None] = relationship(  # pyright: ignore[reportAssignmentType, reportUnknownVariableType]
        model.User,
        backref=backref("likes", cascade="all, delete"),
        uselist=False,
    )

    @override
    def __repr__(self):
        """Internal string representation."""
        return f"<Like of {self.object_type}:{self.object_id} by {self.user_id}>"

    def dictize(self, context: Any) -> dict[str, Any]:
        """Transform object into dictionary."""
        return table_dictize(self, context)

    @classmethod
    def by_object(cls, id: str, type: str) -> sa.sql.Select:
        """Select statement with applied filter by object."""
        return sa.select(cls).where(
            cls.object_id == id,
            cls.object_type == type,
        )

    @classmethod
    def exists(cls, id: str, type: str, user_id: str) -> bool:
        """Select statement with applied filter by object."""
        stmt = (
            sa.select(cls)
            .where(
                cls.object_id == id,
                cls.object_type == type,
                cls.user_id == user_id,
            )
            .exists()
        )

        return model.Session.query(stmt).scalar()

    @classmethod
    def unlike(cls, id: str, type: str, user_id: str) -> bool:
        """Remove like of the user from object."""
        stmt = (
            sa.delete(Like)
            .where(
                cls.object_id == id,
                cls.object_type == type,
                cls.user_id == user_id,
            )
            .returning(Like.object_id)
        )

        return bool(model.Session.scalar(stmt))
