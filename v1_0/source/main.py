import sys
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from transaction import Transaction
from vehicle import Vehicle
from user import User



def Main():
    u = User()
    v = Vehicle()
    v.owner_id = u.id
    v.date_acquired = datetime.now(timezone.utc)
    print(f'user id: {u.id}\n')
    print(f'vehicle id: {v.id}\nvehicle date: {v.date_acquired}')

if __name__ == '__main__':
   Main()