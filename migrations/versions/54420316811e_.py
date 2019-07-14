"""empty message

Revision ID: 54420316811e
Revises: d2ddcccf9741
Create Date: 2019-07-14 02:46:06.448607

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '54420316811e'
down_revision = 'd2ddcccf9741'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(None, 'dutyevent', ['table_date'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'dutyevent', type_='unique')
    # ### end Alembic commands ###
