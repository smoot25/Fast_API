import string
import uuid
from typing import ClassVar, Final


class Base62:
    BASE: Final[ClassVar[str]] = string.ascii_letters + string.digits
    BASE_LEN: Final[ClassVar[int]] = len(BASE)

    @classmethod
    def encode(cls, num: int) -> str:
        if num < 0:
            raise ValueError(
                f"{cls}.encode ()needs positive integer but you passed : {num}"
            )

        if num == 0:
            return cls.BASE[0]
        result = []
        while num:
            num, remainder = divmod(num, cls.BASE_LEN)
            result.append(cls.BASE[remainder])
        return "".join(result)


print(Base62.encode(uuid.uuid4().int))
