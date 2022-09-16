import sys
import time
import aioredis
import asyncio
import logging
logging.basicConfig(filename="publog.txt",filemode = "w",level = logging.INFO)

REDIS_URL = "redis://127.0.0.1:6379" 

#TODO: Remove this hardcoding and take the redis url from environment variables
#TODO: Create an actual gps coords file and test the script
#TODO: Comment the main function

#GPS coordinate file: 
#lat long
#lat long
# and so on


help_message = """
                  Usage: python3 publisher.py path_to_gps_file redis_channel_name time
                    - time should be in seconds
                  example: python3 publisher.py gps_dat.txt gps_dev_23  2
                  """
                
async def main():

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

            logging.info("Starting publisher..")
            for coords in gps_coordinates:
                await redis_client.publish(channel_name,coords)
                logging.info(str(coords))

                if(sleep_time>0):
                    time.sleep(sleep_time)

        except Exception as e:
            print(e)




if(__name__ == "__main__"):
        asyncio.run(main())










