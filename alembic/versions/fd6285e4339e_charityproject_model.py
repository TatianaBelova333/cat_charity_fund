"""CharityProject model

Revision ID: fd6285e4339e
Revises: 
Create Date: 2024-02-05 00:30:51.063907

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd6285e4339e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('charityproject',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('invested_amount', sa.Integer(), nullable=False),
    sa.Column('fully_invested', sa.Boolean(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.Text(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_charityproject_close_date'), 'charityproject', ['close_date'], unique=False)
    op.create_index(op.f('ix_charityproject_create_date'), 'charityproject', ['create_date'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_charityproject_create_date'), table_name='charityproject')
    op.drop_index(op.f('ix_charityproject_close_date'), table_name='charityproject')
    op.drop_table('charityproject')
    # ### end Alembic commands ###