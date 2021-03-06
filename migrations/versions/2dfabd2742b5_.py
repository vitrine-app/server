"""empty message

Revision ID: 2dfabd2742b5
Revises: ec262c266dfe
Create Date: 2018-11-18 18:04:43.761835

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '2dfabd2742b5'
down_revision = 'ec262c266dfe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('companies', 'igdb_id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('companies', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('games', 'igdb_id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('games', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('genres', 'igdb_id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('genres', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    op.alter_column('series', 'igdb_id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=False)
    op.alter_column('series', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('series', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('series', 'igdb_id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('genres', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('genres', 'igdb_id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('games', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('games', 'igdb_id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    op.alter_column('companies', 'name',
               existing_type=mysql.VARCHAR(length=255),
               nullable=True)
    op.alter_column('companies', 'igdb_id',
               existing_type=mysql.BIGINT(display_width=20),
               nullable=True)
    # ### end Alembic commands ###
