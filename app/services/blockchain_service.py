import os
from dotenv import load_dotenv

# load env variables
load_dotenv()

# This is a MOCK blockchain write for hackathon demo
# Later we can replace this with real Polygon code

def store_hash_on_blockchain(record_hash: str) -> bool:
    """
    Simulates storing hash on blockchain.
    For hackathon: this is ENOUGH.
    """

    try:
        # simulate blockchain transaction
        print("🔗 Storing hash on blockchain:")
        print(record_hash)

        # imagine this is written to Polygon testnet
        return True

    except Exception as e:
        print("❌ Blockchain error:", e)
        return False
