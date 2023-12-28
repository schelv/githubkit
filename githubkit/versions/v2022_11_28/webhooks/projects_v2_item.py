"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""

from typing import Dict, Type, Union
from typing_extensions import Annotated, TypeAlias

from pydantic import Field

from githubkit.compat import GitHubModel

from ..models import (
    WebhookProjectsV2ItemEdited,
    WebhookProjectsV2ItemCreated,
    WebhookProjectsV2ItemDeleted,
    WebhookProjectsV2ItemArchived,
    WebhookProjectsV2ItemRestored,
    WebhookProjectsV2ItemConverted,
    WebhookProjectsV2ItemReordered,
)

Event: TypeAlias = Annotated[
    Union[
        WebhookProjectsV2ItemArchived,
        WebhookProjectsV2ItemConverted,
        WebhookProjectsV2ItemCreated,
        WebhookProjectsV2ItemDeleted,
        WebhookProjectsV2ItemEdited,
        WebhookProjectsV2ItemReordered,
        WebhookProjectsV2ItemRestored,
    ],
    Field(discriminator="action"),
]

ProjectsV2ItemEvent: TypeAlias = Event

action_types: Dict[str, Type[GitHubModel]] = {
    "archived": WebhookProjectsV2ItemArchived,
    "converted": WebhookProjectsV2ItemConverted,
    "created": WebhookProjectsV2ItemCreated,
    "deleted": WebhookProjectsV2ItemDeleted,
    "edited": WebhookProjectsV2ItemEdited,
    "reordered": WebhookProjectsV2ItemReordered,
    "restored": WebhookProjectsV2ItemRestored,
}

projects_v2_item_action_types = action_types

__all__ = (
    "Event",
    "ProjectsV2ItemEvent",
    "action_types",
    "projects_v2_item_action_types",
)