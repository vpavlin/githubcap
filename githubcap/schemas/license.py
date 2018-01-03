"""A GitHub user schema."""

from voluptuous import Required
from voluptuous import Url

# pylint: disable=no-value-for-parameter


LICENSE_SCHEMA = {
    Required("key"): str,
    Required("name"): str,
    Required("spdx_id"): str,
    Required("url"): Url()
}
