class ErrorMessages:
    COURIER_DUPLICATE_LOGIN_ERROR = "Этот логин уже используется. Попробуйте другой."
    COURIER_MISSING_FIELDS_ERROR = "Недостаточно данных для создания учетной записи"
    COURIER_LOGIN_MISSING_FIELDS_ERROR = "Недостаточно данных для входа"
    COURIER_NOT_FOUND_ERROR = "Учетная запись не найдена"


class StatusCodes:
    OK = 200
    CREATED_STATUS_CODE = 201
    BAD_REQUEST_STATUS_CODE = 400
    CONFLICT_STATUS_CODE = 409
    NOT_FOUND_STATUS_CODE = 404


class ApiResponses:
    SUCCESS_RESPONSE = {"ok": True}
