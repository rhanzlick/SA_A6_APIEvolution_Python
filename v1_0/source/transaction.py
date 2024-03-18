import sys
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

#from vehicle import Vehicle

def datetime_now() -> datetime:
    return datetime.now(timezone.utc)

class Transaction(BaseModel):
    '''
    Defines a type that represents a transaction through the API.
    '''
    #id: uuid = uuid.uuid4()
    id: UUID = Field(default_factory = uuid4)
    '''
    A unique Id that describes each transaction.
    '''
    
    vehicle_id: UUID = None
    '''
    Id of the vehicle associated to this transaction.
    '''

    description: str = None
    '''
    String description of the transaction
    '''

    cost: float = 0.0

    completed_date: datetime = Field(default_factory = datetime_now)

    @classmethod
    def Create():
        '''
        Save transaction in database.
        '''
        pass

    @classmethod
    def Update():
        '''
        Update existing transaction.
        '''
        pass
    
    @staticmethod
    def Get(id:UUID):
        '''
        Update existing transaction.
        '''
        pass
    
    @classmethod
    def Delete():
        '''
        Delete transaction in database.
        '''
        pass

