"""change student_id into class_id in table students

Revision ID: bc1a49172068
Revises: 
Create Date: 2020-07-09 16:08:53.003796

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'bc1a49172068'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('classes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('class_name', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_classes_class_name'), 'classes', ['class_name'], unique=True)
    op.create_index(op.f('ix_classes_location'), 'classes', ['location'], unique=False)
    op.create_table('students',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('student_name', sa.String(length=64), nullable=True),
    sa.Column('age', sa.Integer(), nullable=True),
    sa.Column('height', sa.Integer(), nullable=True),
    sa.Column('class_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['class_id'], ['classes.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    op.create_index(op.f('ix_students_student_name'), 'students', ['student_name'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_students_student_name'), table_name='students')
    op.drop_table('students')
    op.drop_index(op.f('ix_classes_location'), table_name='classes')
    op.drop_index(op.f('ix_classes_class_name'), table_name='classes')
    op.drop_table('classes')
    # ### end Alembic commands ###