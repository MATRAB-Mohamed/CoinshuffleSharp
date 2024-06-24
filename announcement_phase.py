from participant import Participant

def announcement_phase(participants):
    for participant in participants:
        print(f"Participant {participant.id} announces public key: {participant.public_key}")

