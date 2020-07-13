"""change student_name not to unique

Revision ID: d0d9993bb9e7
Revises: bc1a49172068
Create Date: 2020-07-12 21:46:37.970751

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0d9993bb9e7'
down_revision = 'bc1a49172068'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index('ix_students_student_name', table_name='students')
    op.create_index(op.f('ix_students_student_name'), 'students', ['student_name'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_student_name'), table_name='students')
    op.create_index('ix_students_student_name', 'students', ['student_name'], unique=1)
    # ### end Alembic commands ###
