# Suraksha

## Overview

Suraksha is a minimalistic, low-latency GPS tracking system specifically designed to enable users to track their GPS devices effortlessly. This project aims to provide a reliable and efficient solution for real-time location tracking.

## Features

- User Login with email and password.
- Admin Login with email and password.
- Admin Dashboard to add or remove authorized GPS devices.
- Every authorized GPS device has an unique ID associated with it.
- User can track multiple authorized devices in real time.
- Users can link authorized GPS devices to their account.
- For security and privacy reasons, when an authorized GPS device is linked to account, it cannot be linked to any other account.


## Implementation Details


### Architecture
![GPS Tracking Design](https://github.com/Alok-Joshi/Suraksha/assets/57136069/acd22600-e97f-4a1d-91e0-9c8a71eed9e1)

![Database Schema Diagram](https://github.com/Alok-Joshi/Suraksha/assets/57136069/5111d141-3955-49c0-8222-ed84441305f6)


### Project Structure

The project structure is organized to maintain clarity and facilitate easy development. Here's an overview of the main directories and files:

```
Suraksha
  ├── src/
  │   ├── Suraksha/ 
  │   ├── redis_publisher/
  │
  ├── images/ 
 
```

- `src/`: Contains the source code of the Suraksha project
- `Suraksha/` : Contains the Django source code of the project.
- `redis_publisher/`: Contains a command-line utility to  simulate a GPS device. This provide a good convenience during testing, as an actual physical device is not required. The command-line utility is a python script  that simulates the a GPS device by publishing dummy GPS coordinates to channel.
- `images/`: Holds Project Documentation related images.

### Dependencies

Please check the requirements.txt file for the project dependencies.




