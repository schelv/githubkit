"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union, Literal
from typing_extensions import TypedDict, NotRequired

from .group_0106 import RepositoryRuleUpdateType
from .group_0125 import RepositoryRuleWorkflowsType
from .group_0111 import RepositoryRulePullRequestType
from .group_0103 import OrgRulesetConditionsOneof0Type
from .group_0104 import OrgRulesetConditionsOneof1Type
from .group_0097 import RepositoryRulesetConditionsType
from .group_0096 import RepositoryRulesetBypassActorType
from .group_0123 import RepositoryRuleTagNamePatternType
from .group_0121 import RepositoryRuleBranchNamePatternType
from .group_0109 import RepositoryRuleRequiredDeploymentsType
from .group_0113 import RepositoryRuleRequiredStatusChecksType
from .group_0115 import RepositoryRuleCommitMessagePatternType
from .group_0108 import RepositoryRuleRequiredLinearHistoryType
from .group_0119 import RepositoryRuleCommitterEmailPatternType
from .group_0117 import RepositoryRuleCommitAuthorEmailPatternType
from .group_0105 import (
    RepositoryRuleCreationType,
    RepositoryRuleDeletionType,
    RepositoryRuleNonFastForwardType,
    RepositoryRuleRequiredSignaturesType,
)


class RepositoryRulesetType(TypedDict):
    """Repository ruleset

    A set of rules to apply when specified conditions are met.
    """

    id: int
    name: str
    target: NotRequired[Literal["branch", "tag"]]
    source_type: NotRequired[Literal["Repository", "Organization"]]
    source: str
    enforcement: Literal["disabled", "active", "evaluate"]
    bypass_actors: NotRequired[List[RepositoryRulesetBypassActorType]]
    current_user_can_bypass: NotRequired[
        Literal["always", "pull_requests_only", "never"]
    ]
    node_id: NotRequired[str]
    links: NotRequired[RepositoryRulesetPropLinksType]
    conditions: NotRequired[
        Union[
            RepositoryRulesetConditionsType,
            OrgRulesetConditionsOneof0Type,
            OrgRulesetConditionsOneof1Type,
            None,
        ]
    ]
    rules: NotRequired[
        List[
            Union[
                RepositoryRuleCreationType,
                RepositoryRuleUpdateType,
                RepositoryRuleDeletionType,
                RepositoryRuleRequiredLinearHistoryType,
                RepositoryRuleRequiredDeploymentsType,
                RepositoryRuleRequiredSignaturesType,
                RepositoryRulePullRequestType,
                RepositoryRuleRequiredStatusChecksType,
                RepositoryRuleNonFastForwardType,
                RepositoryRuleCommitMessagePatternType,
                RepositoryRuleCommitAuthorEmailPatternType,
                RepositoryRuleCommitterEmailPatternType,
                RepositoryRuleBranchNamePatternType,
                RepositoryRuleTagNamePatternType,
                RepositoryRuleWorkflowsType,
            ]
        ]
    ]
    created_at: NotRequired[datetime]
    updated_at: NotRequired[datetime]


class RepositoryRulesetPropLinksType(TypedDict):
    """RepositoryRulesetPropLinks"""

    self_: NotRequired[RepositoryRulesetPropLinksPropSelfType]
    html: NotRequired[RepositoryRulesetPropLinksPropHtmlType]


class RepositoryRulesetPropLinksPropSelfType(TypedDict):
    """RepositoryRulesetPropLinksPropSelf"""

    href: NotRequired[str]


class RepositoryRulesetPropLinksPropHtmlType(TypedDict):
    """RepositoryRulesetPropLinksPropHtml"""

    href: NotRequired[str]


__all__ = (
    "RepositoryRulesetType",
    "RepositoryRulesetPropLinksType",
    "RepositoryRulesetPropLinksPropSelfType",
    "RepositoryRulesetPropLinksPropHtmlType",
)
