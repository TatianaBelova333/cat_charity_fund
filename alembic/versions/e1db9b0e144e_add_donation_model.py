"""Add Donation model

Revision ID: e1db9b0e144e
Revises: 1ecd04e5034f
Create Date: 2024-02-05 16:06:04.108776

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e1db9b0e144e'
down_revision = '1ecd04e5034f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('donation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_amount', sa.Integer(), nullable=False),
    sa.Column('invested_amount', sa.Integer(), nullable=False),
    sa.Column('fully_invested', sa.Boolean(), nullable=False),
    sa.Column('create_date', sa.DateTime(), nullable=False),
    sa.Column('close_date', sa.DateTime(), nullable=True),
    sa.Column('comment', sa.Text(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.create_index(batch_op.f('ix_donation_close_date'), ['close_date'], unique=False)
        batch_op.create_index(batch_op.f('ix_donation_create_date'), ['create_date'], unique=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('donation', schema=None) as batch_op:
        batch_op.drop_index(batch_op.f('ix_donation_create_date'))
        batch_op.drop_index(batch_op.f('ix_donation_close_date'))

    op.drop_table('donation')
    # ### end Alembic commands ###
