"""empty message

Revision ID: 5e08fa636493
Revises: 7ad18f1c26a1
Create Date: 2019-03-09 23:42:10.225180

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5e08fa636493'
down_revision = '7ad18f1c26a1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('device_reading', 'reading_cm', new_column_name='reading_mm')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('device_reading', 'reading_mm', new_column_name='reading_cm')
    # ### end Alembic commands ###
