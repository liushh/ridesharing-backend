"""addedfirst version of space

Revision ID: d0207d93e777
Revises: 7e51ac37519d
Create Date: 2018-04-21 15:53:51.307095

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd0207d93e777'
down_revision = '7e51ac37519d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('space',
    sa.Column('created_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_time', sa.DateTime(timezone=True), nullable=True),
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('owner_name', sa.String(length=60), nullable=False),
    sa.Column('owner_id', sa.String(length=60), nullable=True),
    sa.Column('basic_units', sa.String(), nullable=False),
    sa.Column('team', sa.String(length=60), nullable=True),
    sa.Column('space_type', sa.String(length=60), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_space_basic_units'), 'space', ['basic_units'], unique=False)
    op.create_index(op.f('ix_space_owner_id'), 'space', ['owner_id'], unique=False)
    op.create_index(op.f('ix_space_space_type'), 'space', ['space_type'], unique=False)
    op.create_index(op.f('ix_space_team'), 'space', ['team'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_space_team'), table_name='space')
    op.drop_index(op.f('ix_space_space_type'), table_name='space')
    op.drop_index(op.f('ix_space_owner_id'), table_name='space')
    op.drop_index(op.f('ix_space_basic_units'), table_name='space')
    op.drop_table('space')
    # ### end Alembic commands ###
