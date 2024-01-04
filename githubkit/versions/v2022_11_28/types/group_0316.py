"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import TypedDict, NotRequired

from .group_0001 import SimpleUserType


class StargazerType(TypedDict):
    """Stargazer

    Stargazer
    """

    starred_at: datetime
    user: Union[None, SimpleUserType]


__all__ = ("StargazerType",)