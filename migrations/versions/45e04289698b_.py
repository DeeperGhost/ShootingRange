"""empty message

Revision ID: 45e04289698b
Revises: 0c40af5f4a5e
Create Date: 2021-04-01 11:46:21.613335

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '45e04289698b'
down_revision = '0c40af5f4a5e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('EVENTS', sa.Column('id_base_event', sa.Integer(), nullable=True))
    op.add_column('EVENTS', sa.Column('id_base_user', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('EVENTS', 'id_base_user')
    op.drop_column('EVENTS', 'id_base_event')
    # ### end Alembic commands ###
