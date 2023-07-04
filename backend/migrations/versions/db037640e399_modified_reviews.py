"""Modified reviews

Revision ID: db037640e399
Revises: 3034f6c038a5
Create Date: 2023-07-04 12:57:14.450203

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db037640e399'
down_revision = '3034f6c038a5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.alter_column('check_in',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)
        batch_op.alter_column('check_out',
               existing_type=sa.DATETIME(),
               type_=sa.String(),
               existing_nullable=True)

    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.add_column(sa.Column('name', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('email', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('reviews', schema=None) as batch_op:
        batch_op.drop_column('email')
        batch_op.drop_column('name')

    with op.batch_alter_table('bookings', schema=None) as batch_op:
        batch_op.alter_column('check_out',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)
        batch_op.alter_column('check_in',
               existing_type=sa.String(),
               type_=sa.DATETIME(),
               existing_nullable=True)

    # ### end Alembic commands ###
