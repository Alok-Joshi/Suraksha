## User

### Columns:
	- first name
	- last name
	- Email (PRIMARY KEY NOT NULL INDEXING UNIQUE TRUE)
	- Password (Encrypted)

## Device

### Columns:
	- device-mac-address (CANDIDATE KEY)
	- esim phone number (CANDIDATE KEY)
	- device-nick-name (DEFAULT = NULL)
	- device-description  (DEFAULT = NULL)
	- USED (BOOLEAN, INITIAL DEFAULT VALUE = FALSE)

Above table will be created initially with the USED value as False. When a device is added, the table is search and if the entered MAC Address is found, the USED Status is changed
For now, the "uuid" which will be entered by the user for the registration will be the mac-address


## devicedata

### Columns:
	- lattitude
	- longitude
	- device-mac-address (foreign key)

IN DEVELOPMENT


