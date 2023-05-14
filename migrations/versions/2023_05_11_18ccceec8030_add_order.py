"""Create table order

Revision ID: 18ccceec8030
Revises: 
Create Date: 2023-05-12 02:14:39.967535

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '18ccceec8030'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('order',
    sa.Column('order_id', sa.BigInteger(), nullable=False),
    sa.Column('weight', sa.Float(), nullable=False),
    sa.Column('regions', sa.Integer(), nullable=False),
    sa.Column('delivery_hours', sa.ARRAY(sa.String()), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('completed_time', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    # ### end Alembic commands ###