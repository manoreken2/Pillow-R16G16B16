from __future__ import annotations

import warnings


def deprecate(
    deprecated: str,
    when: int | None,
    replacement: str | None = None,
    *,
    action: str | None = None,
    plural: bool = False,
) -> None:
    """
    Deprecations helper.

    :param deprecated: Name of thing to be deprecated.
    :param when: Pillow major version to be removed in.
    :param replacement: Name of replacement.
    :param action: Instead of "replacement", give a custom call to action
        e.g. "Upgrade to new thing".
    :param plural: if the deprecated thing is plural, needing "are" instead of "is".

    Usually of the form:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd).
        Use [new thing] instead."

    You can leave out the replacement sentence:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd)"

    Or with another call to action:

        "[deprecated] is deprecated and will be removed in Pillow [when] (yyyy-mm-dd).
        [Upgrade to new thing]."
    """

    is_ = "are" if plural else "is"

    if when == 10:
        removed = "Pillow 10 (2023-07-01)"
    elif when is None:
        removed = "a future version"
    else:
        raise ValueError(f"Unknown removal version, update {__name__}?")

    if replacement and action:
        raise ValueError("Use only one of 'replacement' and 'action'")

    if replacement:
        action = f". Use {replacement} instead."
    elif action:
        action = f". {action.rstrip('.')}."
    else:
        action = ""

    warnings.warn(
        f"{deprecated} {is_} deprecated and will be removed in {removed}{action}",
        DeprecationWarning,
        stacklevel=3,
    )
