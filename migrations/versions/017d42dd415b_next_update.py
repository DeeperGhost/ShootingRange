"""next update

Revision ID: 017d42dd415b
Revises: e57d03621207
Create Date: 2021-03-17 00:11:53.531418

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '017d42dd415b'
down_revision = 'e57d03621207'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('EventsData_ExerciseID_fkey', 'EventsData', type_='foreignkey')
    op.create_foreign_key(None, 'EventsData', 'Exercise', ['ExerciseID'], ['ExerciseID'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'EventsData', type_='foreignkey')
    op.create_foreign_key('EventsData_ExerciseID_fkey', 'EventsData', 'Exercise', ['ExerciseID'], ['id'])
    # ### end Alembic commands ###
