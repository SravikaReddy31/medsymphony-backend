import hashlib
import json
from datetime import datetime

def generate_health_record_hash(symptoms: str, advice: str) -> str:
    """
    Creates a secure hash for a health record.
    No personal data, only summary text.
    """

    record = {
        "symptoms": symptoms,
        "advice": advice,
        "timestamp": datetime.utcnow().isoformat()
    }

    record_string = json.dumps(record, sort_keys=True)
    record_hash = hashlib.sha256(record_string.encode()).hexdigest()

    return record_hash
