"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class ReposOwnerRepoImportPutBody(GitHubModel):
    """ReposOwnerRepoImportPutBody"""

    vcs_url: str = Field(description="The URL of the originating repository.")
    vcs: Missing[Literal["subversion", "git", "mercurial", "tfvc"]] = Field(
        default=UNSET,
        description="The originating VCS type. Without this parameter, the import job will take additional time to detect the VCS type before beginning the import. This detection step will be reflected in the response.",
    )
    vcs_username: Missing[str] = Field(
        default=UNSET,
        description="If authentication is required, the username to provide to `vcs_url`.",
    )
    vcs_password: Missing[str] = Field(
        default=UNSET,
        description="If authentication is required, the password to provide to `vcs_url`.",
    )
    tfvc_project: Missing[str] = Field(
        default=UNSET,
        description="For a tfvc import, the name of the project that is being imported.",
    )


model_rebuild(ReposOwnerRepoImportPutBody)

__all__ = ("ReposOwnerRepoImportPutBody",)