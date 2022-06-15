"""empty message

Revision ID: abca4eda0f4f
Revises: 0397d41dfeb1
Create Date: 2022-06-15 02:52:37.633881

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'abca4eda0f4f'
down_revision = '0397d41dfeb1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'email')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('email', sa.VARCHAR(length=200), autoincrement=False, nullable=False))
    # ### end Alembic commands ###