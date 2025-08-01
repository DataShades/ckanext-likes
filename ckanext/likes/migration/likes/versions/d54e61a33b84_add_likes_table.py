"""add likes table.

Revision ID: d54e61a33b84
Revises:
Create Date: 2025-08-01 16:16:15.421716

"""

import sqlalchemy as sa
from alembic import op

# revision identifiers, used by Alembic.
revision = "d54e61a33b84"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
        "likes_like",
        sa.Column("object_id", sa.Text(), primary_key=True),
        sa.Column("object_type", sa.Text(), primary_key=True),
        sa.Column(
            "user_id",
            sa.Text(),
            sa.ForeignKey("user.id", ondelete="CASCADE"),
            primary_key=True,
        ),
        sa.Column("created_at", sa.DateTime(True), server_default=sa.func.now()),
        sa.Index("idx_likes_user", "user_id"),
    )


def downgrade():
    op.drop_table("likes_like")
