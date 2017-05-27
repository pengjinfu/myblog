"""empty message

Revision ID: 826f5c61a889
Revises: 207e560dcf69
Create Date: 2017-05-20 14:09:18.461787

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '826f5c61a889'
down_revision = '207e560dcf69'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('loginfo',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('ip', sa.String(length=50), nullable=True),
    sa.Column('time', sa.DateTime(), nullable=True),
    sa.Column('status_code', sa.Integer(), nullable=True),
    sa.Column('length', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(length=200), nullable=True),
    sa.Column('req_time', sa.Float(), nullable=True),
    sa.Column('res_time', sa.Float(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('loginfo')
    # ### end Alembic commands ###