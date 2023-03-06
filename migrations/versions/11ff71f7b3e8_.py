"""empty message

Revision ID: 11ff71f7b3e8
Revises: 46ae45b85116
Create Date: 2023-03-06 09:49:48.498848

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '11ff71f7b3e8'
down_revision = '46ae45b85116'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pokemon', sa.Column('user_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'pokemon', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'pokemon', type_='foreignkey')
    op.drop_column('pokemon', 'user_id')
    # ### end Alembic commands ###