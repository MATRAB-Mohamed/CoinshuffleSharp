from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import random

def encrypt(data, public_key):
    cipher = AES.new(public_key[:16].encode('utf-8'), AES.MODE_CBC)
    if isinstance(data, str):
        data = data.encode('utf-8')
    ct_bytes = cipher.encrypt(pad(data, AES.block_size))
    return cipher.iv + ct_bytes

def shuffling_phase(participants):
    encrypted_addresses = []

    for participant in participants:
        encrypted_address = participant.output_address
        for other_participant in participants:
            encrypted_address = encrypt(encrypted_address, other_participant.public_key)
        encrypted_addresses.append(encrypted_address)

    random.shuffle(encrypted_addresses)

    for i, participant in enumerate(participants):
        participant.encrypted_address = encrypted_addresses[i]
