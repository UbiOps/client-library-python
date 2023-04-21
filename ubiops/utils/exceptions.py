from ..exceptions import UbiOpsException


class BuildStatusError(UbiOpsException, ValueError):
    pass


class ValidateError(UbiOpsException, ValueError):
    pass


class ValidateSkip(UbiOpsException, ValueError):
    pass


class ValidateWarning(UbiOpsException, ValueError):
    pass
