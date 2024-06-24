from ecdsa import SigningKey, SECP256k1
from bitcoinlib.wallets import Wallet

class Participant:
    def __init__(self, participant_id):
        self.id = participant_id
        self.sk, self.vk = self.generate_key_pair()
        self.public_key = self.vk.to_string().hex()
        self.private_key = self.sk.to_string().hex()
        self.output_address = self.generate_bitcoin_address()
        self.encrypted_address = None
        self.signed_message = None

    def generate_key_pair(self):
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.get_verifying_key()
        return sk, vk

    def generate_bitcoin_address(self):
        wallet = Wallet.create('Wallet' + self.id)
        key = wallet.new_key()
        return key.address