"""empty message

Revision ID: 2f69f7ebc55c
Revises: 39fc2c662222
Create Date: 2021-03-25 19:56:44.473246

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2f69f7ebc55c'
down_revision = '39fc2c662222'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('EventsData', sa.Column('reached_rank_id', sa.Float(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('EventsData', 'reached_rank_id')
    # ### end Alembic commands ###
