"""empty message

Revision ID: 3c5318f1a20f
Revises: 6fe925c73763
Create Date: 2024-01-20 17:31:13.325508

"""
import sqlalchemy as sa  # noqa: F401
from alembic import op  # noqa: F401

# revision identifiers, used by Alembic.
revision = "3c5318f1a20f"
down_revision = "6fe925c73763"
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.execute("UPDATE krecik_iot.device SET user_id = 1")
    op.execute("UPDATE krecik_iot.device SET key = 'test'")
    op.alter_column("device", "user_id", existing_type=sa.INTEGER(), nullable=False, schema="krecik_iot")
    op.alter_column("device", "key", existing_type=sa.VARCHAR(), nullable=False, schema="krecik_iot")
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column("device", "key", existing_type=sa.VARCHAR(), nullable=True, schema="krecik_iot")
    op.alter_column("device", "user_id", existing_type=sa.INTEGER(), nullable=True, schema="krecik_iot")
    # ### end Alembic commands ###
