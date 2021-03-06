"""empty message

Revision ID: 6372e68e61ce
Revises: 1c6bdf76963b
Create Date: 2021-03-26 00:36:11.271971

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6372e68e61ce'
down_revision = '1c6bdf76963b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('EventsData', 'reached_rank_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('EventsData', sa.Column('reached_rank_id', sa.INTEGER(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
