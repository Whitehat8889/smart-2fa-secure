# --------------------------------------------------------
# Licensed under the terms of the BSD 3-Clause License
# (see LICENSE for details).
# Copyright © 2021-2025, A.A Suvorov
# All rights reserved.
# --------------------------------------------------------
# https://github.com/smartlegionlab/
# --------------------------------------------------------
import secrets
import string


class CodeGenerator:

    @classmethod
    def generate_code(cls, length: int = 6) -> str:

        if length < 4:
            raise ValueError("The code length must be at least 4 characters..")

        lowercase = string.ascii_lowercase
        uppercase = string.ascii_uppercase
        digits = string.digits
        special_chars = "!@#$%^&*"

        code = [
            secrets.choice(lowercase),
            secrets.choice(uppercase),
            secrets.choice(digits),
            secrets.choice(special_chars)
        ]

        all_chars = lowercase + uppercase + digits + special_chars
        code += [secrets.choice(all_chars) for _ in range(length - 4)]

        secrets.SystemRandom().shuffle(code)

        return ''.join(code)

    def __call__(self, *args, **kwargs):
        return self.generate_code(*args, **kwargs)
