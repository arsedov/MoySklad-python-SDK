class MoyskladError(Exception):
    """Базовый класс исключений библиотеки Moysklad."""
    pass

class AuthError(MoyskladError):
    """Ошибка аутентификации (401)."""
    pass

class RateLimitError(MoyskladError):
    """Слишком много запросов (429)."""
    pass

class APIError(MoyskladError):
    """Ошибка API (400, 404, 500 и т.д.)."""
    def __init__(self, message: str, status_code: int, details: dict | list | None = None):
        super().__init__(message)
        self.status_code = status_code
        self.details = details
