import sys
import time
import logging
import os
from dotenv import load_dotenv
import aioredis
import asyncio

logging.basicConfig(filename="publog.txt",filemode = "w",level = logging.INFO)

load_dotenv("url.env") #will load the environment variables from the .env file in the same dir
REDIS_URL = os.getenv("REDIS_URL")

help_message = """
                  Usage: python3 publisher.py path_to_gps_file redis_channel_name time
                    - time should be in seconds
                  example: python3 publisher.py gps_dat.txt gps_dev_23  2
                  """

async def main():
    """ The main function.It opens the file containing gps_coordinates, loads the coordinates in a list,connects to redis, loops through the coordinates and publishes them to the given channel """
    if(len(sys.argv)>1 and sys.argv[1] == 'help'):
        print(help_message)
        return;
    elif(len(sys.argv) < 4):
        print("Incorrect Number of arguments. Use publisher.py help to see usage ")
        return;
    else:
        try:
            file_path = sys.argv[1]
            channel_name = sys.argv[2]
            sleep_time = float(sys.argv[3])
            logging.info(""" gps_coord file: {file_path} \n redis channel_name : {channel_name} \n sleep time: {sleep_time} \n """)

            redis_client = aioredis.from_url(REDIS_URL)
            gps_coordinates_file = open(file_path,"r")
            gps_coordinates = list(gps_coordinates_file.readlines())

            for coords in gps_coordinates:
                await redis_client.publish(channel_name,coords)
                logging.info(str(coords))
                if(sleep_time>0):
                    time.sleep(sleep_time)

            gps_coordinates_file.close()
        except Exception as e:
            print(e)




if(__name__ == "__main__"):
        asyncio.run(main())










