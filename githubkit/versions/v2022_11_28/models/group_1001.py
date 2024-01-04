"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, ExtraGitHubModel, model_rebuild


class ReposOwnerRepoDeploymentsPostBody(GitHubModel):
    """ReposOwnerRepoDeploymentsPostBody"""

    ref: str = Field(
        description="The ref to deploy. This can be a branch, tag, or SHA."
    )
    task: Missing[str] = Field(
        default=UNSET,
        description="Specifies a task to execute (e.g., `deploy` or `deploy:migrations`).",
    )
    auto_merge: Missing[bool] = Field(
        default=UNSET,
        description="Attempts to automatically merge the default branch into the requested ref, if it's behind the default branch.",
    )
    required_contexts: Missing[List[str]] = Field(
        default=UNSET,
        description="The [status](https://docs.github.com/rest/commits/statuses) contexts to verify against commit status checks. If you omit this parameter, GitHub verifies all unique contexts before creating a deployment. To bypass checking entirely, pass an empty array. Defaults to all unique contexts.",
    )
    payload: Missing[
        Union[ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0, str]
    ] = Field(default=UNSET)
    environment: Missing[str] = Field(
        default=UNSET,
        description="Name for the target deployment environment (e.g., `production`, `staging`, `qa`).",
    )
    description: Missing[Union[str, None]] = Field(
        default=UNSET, description="Short description of the deployment."
    )
    transient_environment: Missing[bool] = Field(
        default=UNSET,
        description="Specifies if the given environment is specific to the deployment and will no longer exist at some point in the future. Default: `false`",
    )
    production_environment: Missing[bool] = Field(
        default=UNSET,
        description="Specifies if the given environment is one that end-users directly interact with. Default: `true` when `environment` is `production` and `false` otherwise.",
    )


class ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0(ExtraGitHubModel):
    """ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0"""


model_rebuild(ReposOwnerRepoDeploymentsPostBody)
model_rebuild(ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0)

__all__ = (
    "ReposOwnerRepoDeploymentsPostBody",
    "ReposOwnerRepoDeploymentsPostBodyPropPayloadOneof0",
)