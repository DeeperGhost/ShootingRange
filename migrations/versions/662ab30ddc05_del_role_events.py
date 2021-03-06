"""del role events

Revision ID: 662ab30ddc05
Revises: 4bfa4fff31fc
Create Date: 2021-04-11 16:56:36.142724

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '662ab30ddc05'
down_revision = '4bfa4fff31fc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('RoleEvents')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('RoleEvents',
    sa.Column('id', sa.INTEGER(), server_default=sa.text('nextval(\'"RoleEvents_id_seq"\'::regclass)'), autoincrement=True, nullable=False),
    sa.Column('id_event', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('id_user', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['id_event'], ['EVENTS.id'], name='RoleEvents_id_event_fkey'),
    sa.ForeignKeyConstraint(['id_user'], ['USERS.id'], name='RoleEvents_id_user_fkey'),
    sa.PrimaryKeyConstraint('id', name='RoleEvents_pkey')
    )
    # ### end Alembic commands ###
