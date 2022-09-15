import sys


help_message = """
                  Usage: python3 publisher.py path_to_gps_file redis_channel_name time
                    - time should be in seconds
                  example: python3 publisher.py gps_dat.txt gps_dev_23  2
                  """
                
def main():

    if(len(sys.argv)>1 and sys.argv[1] == 'help'):
        print(help_message)
        return;
    elif(len(sys.argv) < 4):
        print("Incorrect Number of arguments. Use publisher.py help to see usage ")
        return;

    
    else:
        [ 















if(__name__ == "__main__"):
        main()










