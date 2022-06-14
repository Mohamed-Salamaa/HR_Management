"""empty message

Revision ID: 86aa8ef02381
Revises: 899ecee22865
Create Date: 2022-06-14 19:41:29.413016

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '86aa8ef02381'
down_revision = '899ecee22865'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.add_column('employee', sa.Column('user_name', sa.String(length=200), nullable=False))
    op.add_column('employee', sa.Column('password', sa.String(length=200), nullable=False))
    op.add_column('employee', sa.Column('email', sa.String(length=200), nullable=False))
    op.drop_column('employee', 'employee_department')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('employee_department', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
    op.drop_column('employee', 'email')
    op.drop_column('employee', 'password')
    op.drop_column('employee', 'user_name')
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('user_name', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('password', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    # ### end Alembic commands ###