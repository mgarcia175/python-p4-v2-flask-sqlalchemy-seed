"""Initial migration

Revision ID: 06123c535a24
Revises: 
Create Date: 2024-01-19 23:12:39.620226

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06123c535a24'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('species', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pets')
    # ### end Alembic commands ###