"""empty message

Revision ID: 77c55aa1cd3d
Revises: f7e7721f6d65
Create Date: 2019-07-19 16:18:24.201722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77c55aa1cd3d'
down_revision = 'f7e7721f6d65'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('dutyevent', sa.Column('duty_person', sa.String(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('dutyevent', 'duty_person')
    # ### end Alembic commands ###
