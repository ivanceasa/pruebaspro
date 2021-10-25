"""empty message

Revision ID: 91ae09038b21
Revises: 
Create Date: 2021-10-22 17:17:40.784726

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '91ae09038b21'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('route',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('photo', sa.String(length=250), nullable=True),
    sa.Column('length', sa.String(length=120), nullable=False),
    sa.Column('profile', sa.String(length=250), nullable=False),
    sa.Column('map', sa.String(length=250), nullable=False),
    sa.Column('stages_number', sa.String(length=120), nullable=True),
    sa.Column('start_point', sa.String(length=200), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=120), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('post',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('post_content', sa.String(length=1000), nullable=True),
    sa.Column('date', sa.String(length=120), nullable=False),
    sa.Column('photo', sa.String(length=120), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('stage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('length', sa.String(length=120), nullable=False),
    sa.Column('difficulty', sa.String(length=120), nullable=False),
    sa.Column('photo', sa.String(length=120), nullable=False),
    sa.Column('route_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_route',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('route_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'route_id')
    )
    op.create_table('comment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=300), nullable=True),
    sa.Column('date', sa.String(length=120), nullable=False),
    sa.Column('user_comments', sa.Integer(), nullable=True),
    sa.Column('post_comments', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['post_comments'], ['post.id'], ),
    sa.ForeignKeyConstraint(['user_comments'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('hostel',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=120), nullable=False),
    sa.Column('city', sa.String(length=120), nullable=False),
    sa.Column('photo_hostel', sa.String(length=250), nullable=False),
    sa.Column('phone_number', sa.String(length=120), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=True),
    sa.Column('route_id', sa.Integer(), nullable=True),
    sa.Column('stage_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['route_id'], ['route.id'], ),
    sa.ForeignKeyConstraint(['stage_id'], ['stage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_stage',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('stage_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['stage_id'], ['stage.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'stage_id')
    )
    op.create_table('booking',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('year', sa.Integer(), nullable=False),
    sa.Column('month', sa.Integer(), nullable=False),
    sa.Column('day', sa.Integer(), nullable=False),
    sa.Column('hostel_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['hostel_id'], ['hostel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user_hostel',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('hostel_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['hostel_id'], ['hostel.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('user_id', 'hostel_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_hostel')
    op.drop_table('booking')
    op.drop_table('user_stage')
    op.drop_table('hostel')
    op.drop_table('comment')
    op.drop_table('user_route')
    op.drop_table('stage')
    op.drop_table('post')
    op.drop_table('user')
    op.drop_table('route')
    # ### end Alembic commands ###
