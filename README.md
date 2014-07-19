# Jaalee Rename Utility #

This is a simple utility to encode a human-readable name into the hex-string that should be entered into the Jaalee eBeacon app in order to change the local name of your iBeacon.

The hex code that is generated is your six digit password (the default for Jaalee modules is 0x666666) followed by the hex-encoded new name. The name is padded out to fifteen characters.

To use this utility type `python jaalee_rename.py NEWNAME`. If you have changed the password on your iBeacon, you can type `python jaalee_rename.py NEWNAME PASSWD`. The hex encoded value you should enter into the eBeacon app is displayed as stdout.

In order to use this, I recommend that you copy the code and simply paste it into the control when you are prompted for the new code.

The instructions below for changing the local name value where taken from this page, which has lots of useful information.



1. Convert your new name from ASCII to hexadecimal. 

2. Load the eBeacon app on your apple device.

3. Tap the Central tab on the lower left

4. Tap the jaalee device

5. Scroll down and tap 0xFF80

6. Tap Device name (0x2A00)

7. Tap Write

8. Type your password followed by your new peripheral name. If the name is shorter than 15 characters add 00 for each character until 15 characters are reached. **I recommend that you just paste the value output from the jaylee_rename.py utility here**.

9. Tap Send. Confirmation of sent hex value appears as a box below the write value box with the comment  Select to write.

10. Tapping "Config" at the top left takes you back a screen. 

11. The value box now contains a different value. The first two digits have been over written with a prefix. The 0x01 prefix denotes the value was successfully updated. A 0x00 prefix indicates a write failure, the value has not been updated.

12. Tapping Back -> Services -> eBeacon on the top left disconnects from the device. 



