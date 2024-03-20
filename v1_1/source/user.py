#import sys
from deprecation import deprecated
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from transaction import Transaction
from vehicle import Vehicle
from asset import Asset

def datetime_now() -> datetime:
    return datetime.now(timezone.utc)

class User(BaseModel):
    '''!
    Defines a type that represents a user through the API.
    '''
    
    id: UUID = Field(default_factory = uuid4)
    '''!
    A unique Id that describes each user.
    '''

    username: str = None
    '''!
    String identifier for a user. These also need to be unique amongst all users.
    '''

    email: str = None
    '''!
    Email address of the user.
    '''

    created_date: datetime = None
    '''!
    Account creation date of user
    '''
    
    last_login: datetime = Field(default_factory = datetime_now)
    '''!
    The datetime of latest account access by the user.
    '''

    @classmethod
    def Create() -> bool:
        '''!
        Creates a new User object in the database. Returns true if successful, false otherwise.
        '''
        pass

    @deprecated(deprecated_in = '1.1', details = 'Replaced with the \'Create\' method.')
    @classmethod
    def Craete() -> bool:
        '''! \deprecated Replaced with the \'Create\' method.
        Creates a new User object in the database. Returns true if successful, false otherwise.
        '''
        pass

    @classmethod
    def Update() -> bool:
        '''!
        Updates an existing User object in the database. Returns true if successful, false otherwise.
        '''
        pass

    @classmethod
    def Delete() -> bool:
        '''!
        Removes the user, all associated Vehicle objects, all associated Asset objects, and all subsequently associated Transactions from the database. Returns true if successful, false otherwise.
        '''
        pass

    @classmethod
    def GetAssets(asset_id: Union[UUID, List[UUID]]) -> List[Asset]:
        '''!
        Get all Asset objects associated with this user's id.
        '''
        pass

    @deprecated(deprecated_in = '1.1', details = 'Use of this method should be omitted in favor of the non-static \'GetAssets\' method. Future versions will use the \'Asset\' class in place of all references to the \'Vehicle\' class.')
    @staticmethod
    def GetVehicles(user_id: UUID) -> List[Vehicle]:
        '''! \deprecated Use of this method should be omitted in favor of the non-static \'GetAssets\' method. Future versions will use the \'Asset\' class in place of all references to the \'Vehicle\' class.
        Get all Vehicle objects associated with this user's id.
        '''
        pass

    @classmethod
    def GetUserTransactions(asset_id: Union[UUID, List[UUID]]) -> List[Transaction]:
        '''!
        Get all transactions associated to this user. Optionally, include one or more asset ids to filter the results.
        '''
        pass