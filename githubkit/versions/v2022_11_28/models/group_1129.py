"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class UserMigrationsPostBody(GitHubModel):
    """UserMigrationsPostBody"""

    lock_repositories: Missing[bool] = Field(
        default=UNSET,
        description="Lock the repositories being migrated at the start of the migration",
    )
    exclude_metadata: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether metadata should be excluded and only git source should be included for the migration.",
    )
    exclude_git_data: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether the repository git data should be excluded from the migration.",
    )
    exclude_attachments: Missing[bool] = Field(
        default=UNSET, description="Do not include attachments in the migration"
    )
    exclude_releases: Missing[bool] = Field(
        default=UNSET, description="Do not include releases in the migration"
    )
    exclude_owner_projects: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether projects owned by the organization or users should be excluded.",
    )
    org_metadata_only: Missing[bool] = Field(
        default=UNSET,
        description="Indicates whether this should only include organization metadata (repositories array should be empty and will ignore other flags).",
    )
    exclude: Missing[List[Literal["repositories"]]] = Field(
        default=UNSET,
        description="Exclude attributes from the API response to improve performance",
    )
    repositories: List[str] = Field()


model_rebuild(UserMigrationsPostBody)

__all__ = ("UserMigrationsPostBody",)