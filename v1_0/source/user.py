#import sys
from deprecation import deprecated
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from vehicle import Vehicle

def datetime_now() -> datetime:
    return datetime.now(timezone.utc)

class User(BaseModel):
    '''!
    Defines a type that represents a user through the API.
    '''
    #id: uuid = uuid.uuid4()
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
    def Craete() -> bool:
        '''!
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
        Removes the user, all associated Vehicle objects, and all subsequently associated Transactions from the database. Returns true if successful, false otherwise.
        '''
        pass

    @staticmethod
    def GetVehicles(user_id: UUID, vehicle_id: Union[UUID, List[UUID]]) -> List[Vehicle]:
        '''!
        Get all Vehicle objects associated with this user's id.
        '''
        pass