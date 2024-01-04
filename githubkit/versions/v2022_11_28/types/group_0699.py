"""DO NOT EDIT THIS FILE!

This file is automatically @generated by githubkit using the follow command:

python -m codegen && isort . && black .

See https://github.com/github/rest-api-description for more information.
"""


from __future__ import annotations

from datetime import datetime
from typing import List, Union
from typing_extensions import TypedDict, NotRequired


class WebhookReleasePublishedPropReleaseAllof1Type(TypedDict):
    """WebhookReleasePublishedPropReleaseAllof1"""

    assets: NotRequired[
        List[Union[WebhookReleasePublishedPropReleaseAllof1PropAssetsItemsType, None]]
    ]
    assets_url: NotRequired[str]
    author: NotRequired[WebhookReleasePublishedPropReleaseAllof1PropAuthorType]
    body: NotRequired[Union[str, None]]
    created_at: NotRequired[str]
    draft: NotRequired[bool]
    html_url: NotRequired[str]
    id: NotRequired[int]
    name: NotRequired[Union[str, None]]
    node_id: NotRequired[str]
    prerelease: NotRequired[bool]
    published_at: Union[datetime, None]
    tag_name: NotRequired[str]
    tarball_url: NotRequired[Union[str, None]]
    target_commitish: NotRequired[str]
    upload_url: NotRequired[str]
    url: NotRequired[str]
    zipball_url: NotRequired[Union[str, None]]


class WebhookReleasePublishedPropReleaseAllof1PropAssetsItemsType(TypedDict):
    """WebhookReleasePublishedPropReleaseAllof1PropAssetsItems"""


class WebhookReleasePublishedPropReleaseAllof1PropAuthorType(TypedDict):
    """WebhookReleasePublishedPropReleaseAllof1PropAuthor"""

    avatar_url: NotRequired[str]
    events_url: NotRequired[str]
    followers_url: NotRequired[str]
    following_url: NotRequired[str]
    gists_url: NotRequired[str]
    gravatar_id: NotRequired[str]
    html_url: NotRequired[str]
    id: NotRequired[int]
    login: NotRequired[str]
    node_id: NotRequired[str]
    organizations_url: NotRequired[str]
    received_events_url: NotRequired[str]
    repos_url: NotRequired[str]
    site_admin: NotRequired[bool]
    starred_url: NotRequired[str]
    subscriptions_url: NotRequired[str]
    type: NotRequired[str]
    url: NotRequired[str]


__all__ = (
    "WebhookReleasePublishedPropReleaseAllof1Type",
    "WebhookReleasePublishedPropReleaseAllof1PropAssetsItemsType",
    "WebhookReleasePublishedPropReleaseAllof1PropAuthorType",
)