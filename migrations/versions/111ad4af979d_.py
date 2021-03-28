"""empty message

Revision ID: 111ad4af979d
Revises: 2fc0b8320890
Create Date: 2021-03-28 23:14:10.183459

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '111ad4af979d'
down_revision = '2fc0b8320890'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('EVENTS', sa.Column('end_date', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('EVENTS', 'end_date')
    # ### end Alembic commands ###
