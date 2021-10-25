"""empty message

Revision ID: ff5aea915b71
Revises: 91ae09038b21
Create Date: 2021-10-22 18:49:08.550924

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff5aea915b71'
down_revision = '91ae09038b21'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('profile_picture', sa.String(length=120), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'profile_picture')
    # ### end Alembic commands ###
