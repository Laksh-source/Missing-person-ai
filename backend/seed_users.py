import asyncio
import uuid
from datetime import datetime, timezone
from app.db import get_client
from app.config import settings
from app.security import hash_password

async def seed():
    db = get_client()[settings.mongodb_db]
    users_col = db['users']
    
    seed_data = [
        {
            'id': str(uuid.uuid4()),
            'username': 'admin',
            'email': 'admin@missingperson.ai',
            'password_hash': hash_password('Admin@123'),
            'first_name': 'System',
            'last_name': 'Administrator',
            'role': 'ADMIN',
            'approved': True,
            'ngo_org': None,
            'created_at': datetime.now(timezone.utc)
        },
        {
            'id': str(uuid.uuid4()),
            'username': 'police',
            'email': 'officer@police.gov',
            'password_hash': hash_password('Police@123'),
            'first_name': 'John',
            'last_name': 'Miller',
            'role': 'POLICE',
            'approved': True,
            'ngo_org': None,
            'created_at': datetime.now(timezone.utc)
        },
        {
            'id': str(uuid.uuid4()),
            'username': 'ngo_worker',
            'email': 'worker@hopefoundation.org',
            'password_hash': hash_password('Ngo@123'),
            'first_name': 'Sarah',
            'last_name': 'Connor',
            'role': 'NGO',
            'approved': True,
            'ngo_org': 'Hope Foundation',
            'created_at': datetime.now(timezone.utc)
        },
        {
            'id': str(uuid.uuid4()),
            'username': 'citizen',
            'email': 'citizen@example.com',
            'password_hash': hash_password('Citizen@123'),
            'first_name': 'Alex',
            'last_name': 'Rider',
            'role': 'CITIZEN',
            'approved': True,
            'ngo_org': None,
            'created_at': datetime.now(timezone.utc)
        }
    ]
    
    for u in seed_data:
        existing = await users_col.find_one({'username': u['username']})
        if not existing:
            await users_col.insert_one(u)
            print(f"Created user: {u['username']} ({u['role']})")
        else:
            print(f"User already exists: {u['username']}")

if __name__ == '__main__':
    asyncio.run(seed())
