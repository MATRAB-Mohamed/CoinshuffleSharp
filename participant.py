from ecdsa import SigningKey, SECP256k1
from bitcoinlib.wallets import Wallet, wallets_list
import uuid

class Participant:
    def __init__(self, participant_id):
        self.id = participant_id
        self.sk, self.vk = self.generate_key_pair()
        self.public_key = self.vk.to_string().hex()
        self.private_key = self.sk.to_string().hex()
        self.output_address = self.generate_bitcoin_address()
        self.encrypted_address = None
        self.signed_message = None
    
    @staticmethod
    def get_wallet_count():
        return len(wallets_list())

    def generate_key_pair(self):
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.get_verifying_key()
        return sk, vk

    def generate_bitcoin_address(self):
        wallet_name = f'Wallet_{self.id}_{uuid.uuid4()}'
        wallet = Wallet.create(wallet_name)
        key = wallet.new_key()
        return key.address

# Example usage
# if __name__ == "__main__":
#     NUM_PARTICIPANTS = Participant.get_wallet_count()
#     Num_new_participant = 2

#     participants = [Participant(str(i)) for i in range(NUM_PARTICIPANTS, Num_new_participant + NUM_PARTICIPANTS)]
    
#     for participant in participants:
#         print(f"Participant {participant.id} Bitcoin address:", participant.output_address)
