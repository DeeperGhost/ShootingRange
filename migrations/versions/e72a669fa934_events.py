"""events

Revision ID: e72a669fa934
Revises: f2f4de149d2f
Create Date: 2021-03-04 16:32:14.801249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e72a669fa934'
down_revision = 'f2f4de149d2f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('EVENTS',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_user', sa.Integer(), nullable=False),
    sa.Column('event_name', sa.String(), nullable=False),
    sa.Column('start_date', sa.String(), nullable=False),
    sa.Column('create_date', sa.String(), nullable=False),
    sa.Column('event_status', sa.String(), nullable=True),
    sa.Column('caption', sa.String(), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('EVENTS')
    # ### end Alembic commands ###
