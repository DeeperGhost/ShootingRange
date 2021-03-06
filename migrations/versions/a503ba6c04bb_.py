"""empty message

Revision ID: a503ba6c04bb
Revises: 
Create Date: 2020-12-27 01:31:25.827626

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a503ba6c04bb'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('USERS',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('login', sa.String(), nullable=True),
    sa.Column('email', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('key_pass', sa.String(), nullable=True),
    sa.Column('family', sa.String(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('second_name', sa.String(), nullable=True),
    sa.Column('individual_key', sa.String(), nullable=True),
    sa.Column('information', sa.String(), nullable=True),
    sa.Column('rank', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('USERS')
    # ### end Alembic commands ###
