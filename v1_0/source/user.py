import sys
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

#from transaction import Transaction
from vehicle import Vehicle

def datetime_now() -> datetime:
    return datetime.now(timezone.utc)

class User(BaseModel):
    '''
    Defines a type that represents a user through the API.
    '''
    #id: uuid = uuid.uuid4()
    id: UUID = Field(default_factory = uuid4)
    '''
    A unique Id that describes each user.
    '''

    username: str = None
    '''
    String identifier for a user. These also need to be unique amongst all users.
    '''

    email: str = None
    '''
    Email address of the user.
    '''

    created_date: datetime = None
    '''
    Account creation date of user
    '''
    
    last_login: datetime = Field(default_factory = datetime_now)
    '''
    The datetime of latest account access by the user.
    '''

    @classmethod
    def Craete():
        pass

    @classmethod
    def Update():
        pass

    @classmethod
    def Delete():
        pass

    @staticmethod
    def GetVehicles(user_id: UUID, vehicle_id: Union[UUID, List[UUID]]) -> List[Vehicle]:
        pass



# def Main():
#     u = User()
#     print(u.id)
#     print(datetime.datetime.now())
#     print(sys.path)

#if __name__ == '__main__':
#    Main()