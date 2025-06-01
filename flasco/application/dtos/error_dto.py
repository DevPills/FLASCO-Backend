from http import HTTPStatus

class ServiceError(Exception):
    def __init__(
            self,
            message: str,
            status_code: HTTPStatus,
            headers: dict = None,
            *args: object,
    ) -> None:
        self.message = message
        self.status_code = status_code
        self.headers = headers
        super().__init__(*args)

    def __str__(self):
        return f"{self.status_code}: {self.message}"