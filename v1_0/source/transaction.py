#import sys
from deprecation import deprecated
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

def datetime_now() -> datetime:
    return datetime.now(timezone.utc)

class Transaction(BaseModel):
    '''!
    Defines a type that represents a transaction through the API.
    '''
    
    id: UUID = Field(default_factory = uuid4)
    '''!
    A unique Id that describes each transaction.
    '''
    
    vehicle_id: UUID = None
    '''!
    Id of the vehicle associated to this transaction.
    '''

    description: str = None
    '''!
    String description of the transaction
    '''

    cost: float = 0.0
    '''!
    The financial cost of the transaction in dollars.
    '''

    completed_date: datetime = Field(default_factory = datetime_now)
    '''!
    The date the transaction was completed or performed.
    '''

    @classmethod
    def Create() -> bool:
        '''!
        Save transaction in database. Returns true if successful, false otherwise.
        '''
        pass

    @classmethod
    def Update() -> bool:
        '''!
        Update existing transaction. Returns true if successful, false otherwise.
        '''
        pass
    
    @staticmethod
    def Get(id: UUID) -> bool:
        '''!
        Update existing transaction. Returns true if successful, false otherwise.
        '''
        pass
    
    @classmethod
    def Delete() -> bool:
        '''!
        Delete transaction in database. Returns true if successful, false otherwise.
        '''
        pass

