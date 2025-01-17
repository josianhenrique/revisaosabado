"""empty message

Revision ID: 133fdfd59086
Revises: 
Create Date: 2024-05-06 20:15:12.644782

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '133fdfd59086'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curso',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('unidadecompetencia', schema=None) as batch_op:
        batch_op.alter_column('numero',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('nome',
               existing_type=mysql.VARCHAR(length=250),
               type_=sa.String(length=200),
               nullable=True)
        batch_op.alter_column('carga_horaria',
               existing_type=mysql.INTEGER(),
               nullable=True)
        batch_op.alter_column('competencia_geral',
               existing_type=mysql.VARCHAR(length=250),
               type_=sa.String(length=255),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('unidadecompetencia', schema=None) as batch_op:
        batch_op.alter_column('competencia_geral',
               existing_type=sa.String(length=255),
               type_=mysql.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('carga_horaria',
               existing_type=mysql.INTEGER(),
               nullable=False)
        batch_op.alter_column('nome',
               existing_type=sa.String(length=200),
               type_=mysql.VARCHAR(length=250),
               nullable=False)
        batch_op.alter_column('numero',
               existing_type=mysql.INTEGER(),
               nullable=False)

    op.drop_table('curso')
    # ### end Alembic commands ###
