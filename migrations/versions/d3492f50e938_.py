"""empty message

Revision ID: d3492f50e938
Revises: 
Create Date: 2019-07-17 00:30:58.193655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd3492f50e938'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('timeinterval', sa.Column('time_end2', sa.Time(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('timeinterval', 'time_end2')
    # ### end Alembic commands ###