"""empty message

Revision ID: e82098a270dd
Revises: 708c17369e01
Create Date: 2021-03-21 18:53:56.203033

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e82098a270dd'
down_revision = '708c17369e01'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Exercise', 'kms_f')
    op.drop_column('Exercise', 'msmk_m')
    op.drop_column('Exercise', 'third_f')
    op.drop_column('Exercise', 'third_m')
    op.drop_column('Exercise', 'first_f')
    op.drop_column('Exercise', 'second_f')
    op.drop_column('Exercise', 'first_m')
    op.drop_column('Exercise', 'kms_m')
    op.drop_column('Exercise', 'ms_f')
    op.drop_column('Exercise', 'ms_m')
    op.drop_column('Exercise', 'second_m')
    op.drop_column('Exercise', 'msmk_f')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Exercise', sa.Column('msmk_f', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('second_m', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('ms_m', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('ms_f', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('kms_m', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('first_m', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('second_f', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('first_f', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('third_m', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('third_f', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('msmk_m', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('Exercise', sa.Column('kms_f', sa.INTEGER(), autoincrement=False, nullable=False))
    # ### end Alembic commands ###
