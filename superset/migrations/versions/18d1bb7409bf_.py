"""empty message

Revision ID: 18d1bb7409bf
Revises: 55e910a74826
Create Date: 2018-11-28 15:59:04.305305

"""

# revision identifiers, used by Alembic.
revision = '18d1bb7409bf'
down_revision = '55e910a74826'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('visitor',
    sa.Column('created_on', sa.DateTime(), nullable=True),
    sa.Column('changed_on', sa.DateTime(), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('jbh_uid', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=10), nullable=True),
    sa.Column('phone', sa.String(length=15), nullable=True),
    sa.Column('group_prop', sa.String(length=10), nullable=True),
    sa.Column('registry_type', sa.Integer(), nullable=True),
    sa.Column('first_vistor_time', sa.Date(), nullable=True),
    sa.Column('first_receptor', sa.String(length=10), nullable=True),
    sa.Column('illustration', sa.Text(), nullable=True),
    sa.Column('communication_times', sa.Integer(), nullable=True),
    sa.Column('deal_times', sa.Integer(), nullable=True),
    sa.Column('agree', sa.Boolean(), nullable=True),
    sa.Column('status', sa.String(length=10), nullable=True),
    sa.Column('created_by_fk', sa.Integer(), nullable=True),
    sa.Column('changed_by_fk', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['changed_by_fk'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['created_by_fk'], ['ab_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('vistorreg_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('vistorreg_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['ab_user.id'], ),
    sa.ForeignKeyConstraint(['vistorreg_id'], ['visitor.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('vistorreg_user')
    op.drop_table('visitor')
    # ### end Alembic commands ###
