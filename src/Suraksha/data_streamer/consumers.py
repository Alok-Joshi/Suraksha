from channels.generic.websocket import AsyncWebsocketConsumer
import aioredis


class gps_coordinates(AsyncWebsocketConsumer):

    def get_channel_name(self,device_name):
        return "{device_name}_channel"

    async def connect(self):

        #TODO: 1) Get the device name from the scope, 2) subscribe to the appropriate channel name (get channel name from device name , 3) create the neccessary pubsub objects 
        pass

    async def receive(self,text_data):
        pass

    async def disconnect(self, close_code):
        pass
