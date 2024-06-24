from blame_phase import blame_phase


def sign(transaction, private_key):
    # Mock function for signing a transaction
    return f"signed_{transaction}_with_{private_key}"

def combine_signatures(transaction, signatures):
    # Mock function for combining signatures
    return f"{transaction}_with_signatures_{'_'.join(signatures)}"

def broadcast_transaction(transaction):
    print(f"Broadcasting transaction: {transaction}")

def broadcasting_phase(participants, transaction):
    signatures = []

    for participant in participants:
        signature = sign(transaction, participant.private_key)
        signatures.append(signature)

    if len(signatures) == len(participants):
        final_transaction = combine_signatures(transaction, signatures)
        broadcast_transaction(final_transaction)
    else:
        print("Not all signatures collected, invoking blame phase")
        blame_phase()