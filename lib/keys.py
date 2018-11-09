import os
import re
from base64 import b64decode
from nacl.secret import SecretBox


def populate_keys():
    secret_key = os.getenv('VITRINE_KEY')
    if secret_key is None:
        raise KeyError('VITRINE_KEY env variable is missing.')
    fd = open(os.getcwd() + '/lib/vault.keys', 'r')
    key_lines = fd.read().split('\n')
    key_lines.pop()
    for key_line in key_lines:
        match = re.search('([A-Z_]+)=(.*)', key_line)
        key_name = match.group(1) + '_KEY'
        key = match.group(2)
        encrypted = key.split(':')
        nonce = b64decode(encrypted[0])
        encrypted = b64decode(encrypted[1])
        box = SecretBox(bytes(secret_key, encoding='utf8'))
        decrypted = box.decrypt(encrypted, nonce).decode('utf-8')
        os.environ[key_name] = decrypted
