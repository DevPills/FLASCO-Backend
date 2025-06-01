"""Recriada após exclusão acidental

Revision ID: 507c4971812b
Revises: df23133e6bc0
Create Date: 2025-05-31 18:00:52.574925
"""

from alembic import op
import sqlalchemy as sa
from typing import Sequence, Union

# revision identifiers, used by Alembic.
revision: str = '507c4971812b'
down_revision: Union[str, None] = 'df23133e6bc0'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None

def upgrade() -> None:
    pass  # ou adicione os comandos executados aqui, se souber

def downgrade() -> None:
    pass  # ou implemente reversão, se necessário
