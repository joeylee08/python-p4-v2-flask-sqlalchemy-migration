"""added departments table

Revision ID: 4122401c5a64
Revises: ca7a1f823da1
Create Date: 2023-11-13 10:04:53.109329

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4122401c5a64'
down_revision = 'ca7a1f823da1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
