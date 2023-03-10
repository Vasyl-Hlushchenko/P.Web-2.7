"""Init

Revision ID: f072ecfb6b29
Revises: ff5016b4d877
Create Date: 2023-01-15 21:31:58.116066

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "f072ecfb6b29"
down_revision = "ff5016b4d877"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "groups", sa.Column("group_name", sa.String(length=150), nullable=False)
    )
    op.drop_column("groups", "group_nam")
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "groups",
        sa.Column(
            "group_nam", sa.VARCHAR(length=150), autoincrement=False, nullable=False
        ),
    )
    op.drop_column("groups", "group_name")
    # ### end Alembic commands ###
