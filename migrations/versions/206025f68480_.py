"""empty message

Revision ID: 206025f68480
Revises: fec7d73081bf
Create Date: 2020-05-13 23:57:29.496296

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '206025f68480'
down_revision = 'fec7d73081bf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('Show_artist_image_link_key', 'Show', type_='unique')
    op.drop_constraint('Show_artist_name_key', 'Show', type_='unique')
    op.drop_constraint('Show_venue_image_link_key', 'Show', type_='unique')
    op.drop_constraint('Show_venue_name_key', 'Show', type_='unique')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('Show_venue_name_key', 'Show', ['venue_name'])
    op.create_unique_constraint('Show_venue_image_link_key', 'Show', ['venue_image_link'])
    op.create_unique_constraint('Show_artist_name_key', 'Show', ['artist_name'])
    op.create_unique_constraint('Show_artist_image_link_key', 'Show', ['artist_image_link'])
    # ### end Alembic commands ###
