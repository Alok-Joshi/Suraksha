from typing import get_args
from channels.consumer import get_channel_layer
from channels.generic.websocket import AsyncWebsocketConsumer
from Suraksha.settings import REDIS_URL
import aioredis
import json
import pdb

class gps_coordinates(AsyncWebsocketConsumer):

    def process_coordinates(self,coordinates):
        """ Parses the coordinates recieved from the redis . Returns a dictionary: {lat: val, long: val} """
        return coordinates
        pass

    def get_channel_name(self,device_name):
        return f"{device_name}_channel"

    async def connect(self):
        """ Gets the device name and subscribes to the appropriate device name to get the gps coordinates """
        try:
            await self.accept()
            self.device_name = self.scope['url_route']['kwargs']['device_name']
            self.channel_name = self.get_channel_name(self.device_name)
            self.redis_client = aioredis.from_url(REDIS_URL,decode_responses = True)
            self.pubsub = self.redis_client.pubsub()

            await self.pubsub.subscribe(self.channel_name)

        except Exception as e:
            print(e)

    async def receive(self,text_data):

        try:
            redis_coordinate_data = await self.pubsub.get_message(ignore_subscribe_messages = True)
            coordinates = self.process_coordinates(redis_coordinate_data)
            message = json.dumps(coordinates)
            await self.send(message)

        except Exception as e:
            print(e)




    async def disconnect(self, close_code):

        await self.redis_client.close()
