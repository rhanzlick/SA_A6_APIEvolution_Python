#import sys
from deprecation import deprecated
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

#from vehicle import Vehicle

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

    asset_id: UUID = None
    '''!
    Id of the associated asset. This should be used in lieu of the deprecated \'vehicle_id\' property.
    '''

    #@deprecated(deprecated_in='1.1', details='Use of this property should be omitted in favor of the \'asset_id\' property.')
    ## \deprecated This property is deprecated as of version 1.1, and its use should be avoided in favor of the \'asset_id\' property.
    vehicle_id: UUID = None
    '''! \deprecated Use of this property should be omitted in favor of the \'asset_id\' property.
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
    
    @deprecated(deprecated_in = '1.1', details = 'Use of this static method should be omitted. It will be removed in a future version.')
    @staticmethod
    def Get(id: UUID) -> bool:
        '''! \deprecated Use of this static method should be omitted. It will be removed in a future version.
        Update existing transaction. Returns true if successful, false otherwise.
        '''
        pass
    
    @classmethod
    def Delete() -> bool:
        '''!
        Delete transaction in database. Returns true if successful, false otherwise.
        '''
        pass

