from flasco.repositories.favorito_repository import FavoritoRepository


class PutFavoriteUseCase: 
    def __init__(
        self,
        favorito_repository: FavoritoRepository,
    ):
        self.favorito_repository= favorito_repository
    
    async def execute(self, id_modulo: str):
                return