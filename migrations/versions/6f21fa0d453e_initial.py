"""initial

Revision ID: 6f21fa0d453e
Revises: 
Create Date: 2018-07-15 22:32:48.586139

"""
from alembic import op
import sqlalchemy as sa
import sq.ext.rdbms.types


# revision identifiers, used by Alembic.
revision = '6f21fa0d453e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('onetimepasswords',
    sa.Column('gsid', sq.ext.rdbms.types.UUID(), nullable=False),
    sa.Column('nsid', sa.String(), nullable=False),
    sa.Column('generated', sa.BigInteger(), nullable=False),
    sa.Column('kind', sa.String(), nullable=False),
    sa.Column('secret', sa.String(), nullable=False),
    sa.Column('counter', sa.Integer(), nullable=False),
    sa.Column('issuer', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('gsid')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('onetimepasswords')
    # ### end Alembic commands ###
