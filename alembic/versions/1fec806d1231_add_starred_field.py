"""add starred field

Revision ID: 1fec806d1231
Revises: 
Create Date: 2021-07-24 13:47:06.431195

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "1fec806d1231"
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("items", sa.Column("starred", sa.Boolean, nullable=True))
    op.execute("UPDATE items SET starred = false")
    op.alter_column("items", "starred", nullable=False)


def downgrade():
    with op.batch_alter_table("items", schema=None) as batch_op:
        batch_op.drop_column("starred")
