"""Initial migration

Revision ID: 09c97ce08894
Revises: 
Create Date: 2025-03-22 12:52:58.029560

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '09c97ce08894'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('analysis', schema=None) as batch_op:
        batch_op.alter_column('file_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    with op.batch_alter_table('financial_file', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('financial_file', schema=None) as batch_op:
        batch_op.alter_column('user_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    with op.batch_alter_table('analysis', schema=None) as batch_op:
        batch_op.alter_column('file_id',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###
