"""next update2

Revision ID: e57d03621207
Revises: ebe62e210240
Create Date: 2021-03-17 00:09:04.186541

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e57d03621207'
down_revision = 'ebe62e210240'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'Exercise', ['ExerciseID'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'Exercise', type_='unique')
    # ### end Alembic commands ###
