"""restrição aluno_id no se_matricula

Revision ID: a1d4a58297f7
Revises: 507c4971812b
Create Date: 2025-05-31 19:10:14.113522

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a1d4a58297f7'
down_revision: Union[str, None] = '507c4971812b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.drop_constraint('se_matricula_id_aluno_fkey', 'se_matricula', type_='foreignkey')
    op.create_foreign_key(
        'fk_se_matricula_id_aluno_aluno',
        'se_matricula', 'aluno',
        ['id_aluno'], ['id_usuario']
    )


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
