"""flask security next

Revision ID: 1888d0caf41d
Revises: 7ca143d43b4c
Create Date: 2021-03-27 00:49:09.506646

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1888d0caf41d'
down_revision = '7ca143d43b4c'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('USERS', sa.Column('active', sa.Boolean(), nullable=True))
    op.add_column('USERS', sa.Column('confirmed_at', sa.DateTime(), nullable=True))
    op.add_column('USERS', sa.Column('current_login_at', sa.DateTime(), nullable=True))
    op.add_column('USERS', sa.Column('current_login_ip', sa.String(length=100), nullable=True))
    op.add_column('USERS', sa.Column('last_login_at', sa.DateTime(), nullable=True))
    op.add_column('USERS', sa.Column('last_login_ip', sa.String(length=100), nullable=True))
    op.add_column('USERS', sa.Column('login_count', sa.Integer(), nullable=True))
    op.add_column('USERS', sa.Column('password', sa.String(length=255), nullable=True))
    op.add_column('USERS', sa.Column('username', sa.String(length=255), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('USERS', 'username')
    op.drop_column('USERS', 'password')
    op.drop_column('USERS', 'login_count')
    op.drop_column('USERS', 'last_login_ip')
    op.drop_column('USERS', 'last_login_at')
    op.drop_column('USERS', 'current_login_ip')
    op.drop_column('USERS', 'current_login_at')
    op.drop_column('USERS', 'confirmed_at')
    op.drop_column('USERS', 'active')
    # ### end Alembic commands ###
