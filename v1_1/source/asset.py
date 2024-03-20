#import sys
from deprecation import deprecated
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from transaction import Transaction

class Asset(BaseModel):
    '''!
    Defines a type that represents an Asset through the API.
    '''
    
    id: UUID = Field(default_factory = uuid4)
    '''!
    A unique Id that describes each Asset.
    '''
    
    owner_id: UUID = None
    '''!
    Id of the current owner associated to this Asset.
    '''

    asset_description:str = ''
    '''!
    A text description of the asset.
    '''

    asset_type:str = ''
    '''!
    A text description for the type of asset. e.g. \'Vehicle\' or \'House\'
    '''

    date_acquired: datetime = None
    '''!
    Date that the current user gained possession of this Asset.
    '''

    features: dict = {}
    '''!
    A flexible implementation of potential properties associated to this Asset.
    '''

    @classmethod
    def Create() -> bool:
        '''!
        Create a new Asset object in the database. Returns true if successful, false otherwise.
        '''
        pass

    @classmethod
    def Update() -> bool:
        '''!
        Update existing Asset in the database. Returns true if successful, false otherwise.
        '''
        pass

    @classmethod
    def GetTransactions() -> List[Transaction]:
        '''!
        Get all transactions associated to this Asset's id.
        '''
        pass

