#import sys
from deprecation import deprecated
from typing import List, Union
from pydantic import BaseModel, Field
from datetime import datetime, timezone
from uuid import UUID, uuid4

from transaction import Transaction

@deprecated(deprecated_in = '1.1', details = 'Use of class should be omitted in favor to the new \'Asset\' class.')
class Vehicle(BaseModel):
    '''
    Defines a type that represents a vehicle through the API.
    '''
    #id: uuid = uuid.uuid4()
    id: UUID = Field(default_factory = uuid4)
    '''
    A unique Id that describes each vehicle.
    '''
    
    owner_id: UUID = None
    '''
    Id of the current owner associated to this vehicle.
    '''

    date_acquired: datetime = None
    '''
    Date that the current user gained possession of this vehicle.
    '''

    vin: str = None
    '''
    Vin number associated to the vehicle.
    '''

    manufacturer: str = None
    '''
    The name of the manufacturer of the vehicle.
    '''

    model: str = None
    '''
    The name of the model of the vehicle.
    '''

    year: int = None
    '''
    The year the vehicle was created.
    '''

    @classmethod
    def Create() -> bool:
        '''
        Create a new Vehicle object in the database. Returns true if successful, false otherwise.
        '''
        pass

    @classmethod
    def Update() -> bool:
        '''
        Update existing Vehicle in the database. Returns true if successful, false otherwise.
        '''
        pass

    @classmethod
    def GetTransactions() -> List[Transaction]:
        '''
        Get all transactions associated to this vehicle's id.
        '''
        pass

    @deprecated(deprecated_in = '1.1', details = 'Use of this static method should be omitted in favor of the non-static variant with the same name.')
    @staticmethod
    def GetTransactions(vehicle_id: Union[UUID, List[UUID]]) -> List[Transaction]:
        '''
        Get all transactions associated to this vehicle's id.
        '''
        pass

