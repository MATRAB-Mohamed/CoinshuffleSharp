from participant import Participant
from announcement_phase import announcement_phase
from shuffling_phase import shuffling_phase
from transaction_verification_phase import transaction_verification_phase
from broadcasting_phase import broadcasting_phase
from blame_phase import blame_phase

NUM_PARTICIPANTS = Participant.get_wallet_count()
Num_new_participant = int(input('Entrer le nombre des participants : '))

def main():
    # Initialize participants
    participants = [Participant(str(i)) for i in range(NUM_PARTICIPANTS, Num_new_participant + NUM_PARTICIPANTS)]

    # Phase 1: Announcement
    print("Announcement Phase")
    announcement_phase(participants)

    # Phase 2: Shuffling
    print("Shuffling Phase")
    shuffling_phase(participants)

    # Phase 3: Transaction Verification
    print("Transaction Verification Phase")
    transaction = transaction_verification_phase(participants)
    if transaction:
        # Phase 4: Broadcasting
        print("Broadcasting Phase")
        broadcasting_phase(participants, transaction)
    else:
        # If transaction verification fails, initiate blame phase
        print("Transaction verification failed, initiating Blame Phase")
        blame_phase()

if __name__ == "__main__":
    main()
