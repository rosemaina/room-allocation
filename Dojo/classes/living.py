from dojoRoom import Room
class LivingSpace(Room):

    def __init__(self,room_name, room_type='living_space', room_capacity=4):
        super(LivingSpace, self).__init__(room_name, room_type, room_capacity)
