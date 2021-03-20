"""empty message

Revision ID: 9648179a2404
Revises: 35ac2a786055
Create Date: 2019-07-19 20:31:33.762241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9648179a2404'
down_revision = '35ac2a786055'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('testdutyevent',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('duty_type_id', sa.Integer(), nullable=True),
    sa.Column('duty_person_id', sa.Integer(), nullable=True),
    sa.Column('duty_person', sa.String(), nullable=True),
    sa.Column('date_time_start', sa.DateTime(), nullable=False),
    sa.Column('date_time_stop', sa.DateTime(), nullable=False),
    sa.Column('date_ym', sa.String(), nullable=False),
    sa.Column('date_ymd', sa.String(), nullable=False),
    sa.Column('table_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['duty_person_id'], ['person.id'], ),
    sa.ForeignKeyConstraint(['duty_type_id'], ['dutytype.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('testdutyevent')
    # ### end Alembic commands ###