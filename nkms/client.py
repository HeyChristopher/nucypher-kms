class Client(object):
    """
    Client which will be used by Python developers to interact with the
    decentralized KMS. For now, this is just the skeleton.
    """

    def __init__(self, conf=None):
        """
        :param str conf: Config file to load/save the key information from. If
            not given, a default one in the home directory is used
            or created
        """
        pass

    def encrypt(self, data, path=None, algorithm=None):
        """
        Encrypts data in a form ready to ship to the storage layer.

        :param bytes data: Data to encrypt
        :param tuple(str) path: Path to the data (to be able to share
            sub-paths). If None, encrypted with just our pubkey.
            If contains only 1 element or is a string, this is just used as a
            unique identifier w/o granular encryption.
        :param dict algorithm: Algorithm parameters (name, curve, re-encryption
            type, m/n etc). None if default

        :return: Encrypted data
        :rtype: bytes
        """
        pass

    def decrypt(self, edata, path=None, owner=None):
        """
        Decrypt data encrypted by its owner. If the owner != ourselves, a
        re-encryption request is automatically submitted. The function
        automatically splits out encrypted symmetric keys.

        :param bytes edata: Encrypted data
        :param tuple(str) path: Path to the data or its identifier
        :param bytes owner: If the path is None, owner can be used to identify
            the re-encryption key. The owner is specified by his pubkey

        :return: Unencrypted data
        :rtype: bytes
        """
        pass

    def delegate(self, pubkey, path=None, policy=None):
        """
        Allow pubkey to read the data by path (or everything) by creating the
        re-encryption key and submitting it to the network.

        :param bytes pubkey: Public key of who we share the data with
        :param tuple(str) path: Path which we share. If None - share everything
        :param dict policy: Policy for sharing. For now, can have start_time and
            stop_time (in Python datetime or unix time (int))
        """
        pass

    def revoke(self, pubkey, path=None):
        """
        Revoke a currently existing policy. Tells re-encryption nodes to remove
        the corresponding rekeys.

        :param bytes pubkey: Public key of who we shared the data with
        :param tuple(str) path: Path which we share. If None - revoke everything
        """
        pass