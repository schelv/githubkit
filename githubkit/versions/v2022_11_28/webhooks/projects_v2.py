"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.utils import TaggedUnion
from githubkit.compat import GitHubModel

from ..models import (
    WebhookProjectsV2ProjectClosed,
    WebhookProjectsV2ProjectEdited,
    WebhookProjectsV2ProjectCreated,
    WebhookProjectsV2ProjectDeleted,
    WebhookProjectsV2ProjectReopened,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookProjectsV2ProjectClosed,
        WebhookProjectsV2ProjectCreated,
        WebhookProjectsV2ProjectDeleted,
        WebhookProjectsV2ProjectEdited,
        WebhookProjectsV2ProjectReopened,
    ],
    Field(discriminator="action"),
]

ProjectsV2Event: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "closed": WebhookProjectsV2ProjectClosed,
    "created": WebhookProjectsV2ProjectCreated,
    "deleted": WebhookProjectsV2ProjectDeleted,
    "edited": WebhookProjectsV2ProjectEdited,
    "reopened": WebhookProjectsV2ProjectReopened,
}

projects_v2_action_types = action_types

__all__ = ("Event", "ProjectsV2Event", "action_types", "projects_v2_action_types")
