class NoPrivateKeyException(Exception):
    """
    No private key was provided so unable to perform any operations requiring message signing.

    """

    pass


class DigitalTwinMapException(Exception):
    """
    No Digital Twin was created with this index or there is no such topic in Digital Twin map.

    """

    pass


class InvalidExtrinsicHash(Exception):
    """
    Invalid extrinsic hash format. Hash length is not 66 signs, or it doesn't start from 0x.

    """

    pass


class InvalidExtrinsicIndex(Exception):
    """
    Invalid extrinsic index for block lookup.
    """

    pass


class AmbiguousExtrinsicSubmissionException(Exception):
    """
    The node connection was lost after submitting an extrinsic.

    The transaction may have reached the node, so the library must not submit it
    again automatically.
    """

    def __init__(self, message: str, extrinsic_hash=None):
        self.extrinsic_hash = extrinsic_hash
        super().__init__(message)
