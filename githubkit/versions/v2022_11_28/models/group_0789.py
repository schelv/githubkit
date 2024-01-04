"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from typing import List, Union, Literal

from pydantic import Field

from githubkit.utils import UNSET
from githubkit.typing import Missing
from githubkit.compat import GitHubModel, model_rebuild


class WebhookWorkflowJobInProgressPropWorkflowJobAllof1(GitHubModel):
    """WebhookWorkflowJobInProgressPropWorkflowJobAllof1"""

    check_run_url: Missing[str] = Field(default=UNSET)
    completed_at: Missing[Union[str, None]] = Field(default=UNSET)
    conclusion: Missing[Union[str, None]] = Field(default=UNSET)
    created_at: Missing[str] = Field(
        default=UNSET, description="The time that the job created."
    )
    head_sha: Missing[str] = Field(default=UNSET)
    html_url: Missing[str] = Field(default=UNSET)
    id: Missing[int] = Field(default=UNSET)
    labels: Missing[List[str]] = Field(default=UNSET)
    name: Missing[str] = Field(default=UNSET)
    node_id: Missing[str] = Field(default=UNSET)
    run_attempt: Missing[int] = Field(default=UNSET)
    run_id: Missing[int] = Field(default=UNSET)
    run_url: Missing[str] = Field(default=UNSET)
    runner_group_id: Missing[Union[int, None]] = Field(default=UNSET)
    runner_group_name: Missing[Union[str, None]] = Field(default=UNSET)
    runner_id: Missing[Union[int, None]] = Field(default=UNSET)
    runner_name: Missing[Union[str, None]] = Field(default=UNSET)
    started_at: Missing[str] = Field(default=UNSET)
    status: Literal["in_progress", "completed", "queued"] = Field()
    head_branch: Missing[Union[str, None]] = Field(
        default=UNSET, description="The name of the current branch."
    )
    workflow_name: Missing[Union[str, None]] = Field(
        default=UNSET, description="The name of the workflow."
    )
    steps: List[
        WebhookWorkflowJobInProgressPropWorkflowJobAllof1PropStepsItems
    ] = Field()
    url: Missing[str] = Field(default=UNSET)


class WebhookWorkflowJobInProgressPropWorkflowJobAllof1PropStepsItems(GitHubModel):
    """Workflow Step"""

    completed_at: Union[str, None] = Field()
    conclusion: Union[str, None] = Field()
    name: str = Field()
    number: int = Field()
    started_at: Union[str, None] = Field()
    status: Literal["in_progress", "completed", "pending", "queued"] = Field()


model_rebuild(WebhookWorkflowJobInProgressPropWorkflowJobAllof1)
model_rebuild(WebhookWorkflowJobInProgressPropWorkflowJobAllof1PropStepsItems)

__all__ = (
    "WebhookWorkflowJobInProgressPropWorkflowJobAllof1",
    "WebhookWorkflowJobInProgressPropWorkflowJobAllof1PropStepsItems",
)