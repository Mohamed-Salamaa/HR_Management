"""empty message

Revision ID: 2d8b9ecedf7f
Revises: abca4eda0f4f
Create Date: 2022-06-15 02:57:24.315389

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2d8b9ecedf7f'
down_revision = 'abca4eda0f4f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('employee', sa.Column('check_login', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('employee', 'check_login')
    # ### end Alembic commands ###
