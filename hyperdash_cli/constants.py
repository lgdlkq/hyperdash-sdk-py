import os

import six


def get_base_url():
    return six.text_type(os.environ.get(
        "HYPERDASH_SERVER",
        "https://hyperdash.io/api/v1",
    ))
