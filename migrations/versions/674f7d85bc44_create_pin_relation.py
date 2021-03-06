"""Create pin relation

Revision ID: 674f7d85bc44
Revises: a8eb8a00d632
Create Date: 2018-09-08 19:09:35.139586

"""
from alembic import op
import sqlalchemy as sa
import sq.ext.rdbms.types


# revision identifiers, used by Alembic.
revision = '674f7d85bc44'
down_revision = 'a8eb8a00d632'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('pin',
    sa.Column('gsid', sq.ext.rdbms.types.UUID(), nullable=False),
    sa.Column('pin', sa.String(), nullable=False),
    sa.Column('failed', sa.Integer(), nullable=False),
    sa.Column('last_used', sa.BigInteger(), nullable=False),
    sa.PrimaryKeyConstraint('gsid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('pin')
    # ### end Alembic commands ###
