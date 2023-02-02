# Tray menu to control all your tuya enabled lights.
First of all you need to create the snapshot.json file, using the instructions from the tinituya project page:

# Setup Wizard - Getting Local Keys
TinyTuya has a built-in setup Wizard that uses the Tuya IoT Cloud Platform to generate a JSON list (devices.json) of all your registered devices, including secret Local_Key and Name of your devices. Follow the steps below:

PAIR - Download the Smart Life App or Tuya Smart App, available for iPhone or Android. Pair all of your Tuya devices (this is important as you cannot access a device that has not been paired).

SCAN - Run the TinyTuya scan to get a list of Tuya devices on your network. It will show device Address, Device ID and Version number (3.1 or 3.3):

python -m tinytuya scan
NOTE: You will need to use one of the displayed Device IDs for step 4.

TUYA ACCOUNT - Set up a Tuya Account (see PDF Instructions):

NOTE: Tuya often changes their portal and services. Please open an issue with screenshots if we need to update these instructions.
Create a Tuya Developer account on iot.tuya.com. When it asks for the "Account Type", select "Skip this step..." (see screenshot).
Click on "Cloud" icon -> "Create Cloud Project"
Remember the "Data Center" you select. This will be used by TinyTuya Wizard (screenshot).
Skip the configuration wizard but remember the Authorization Key: API ID and Secret for below (screenshot).
Click on "Cloud" icon -> Select your project -> Devices -> Link Tuya App Account (see screenshot)
Click Add App Account (screenshot) and it will display a QR code. Scan the QR code with the Smart Life app on your Phone (see step 1 above) by going to the "Me" tab in the Smart Life app and clicking on the QR code button [..] in the upper right hand corner of the app. When you scan the QR code, it will link all of the devices registered in your Smart Life app into your Tuya IoT project.
NO DEVICES? If no devices show up after scanning the QR code, you will need to select a different data center and edit your project (or create a new one) until you see your paired devices from the Smart Life App show up. (screenshot). The data center may not be the most logical. As an example, some in the UK have reported needing to select "Central Europe" instead of "Western Europe".
SERVICE API: Under "Service API" ensure these APIs are listed: IoT Core, Authorization and Smart Home Scene Linkage. To be sure, click subscribe again on every service. Very important: disable popup blockers otherwise subscribing won't work without providing any indication of a failure. Make sure you authorize your Project to use those APIs:
Click "Service API" tab
Click "Go to Authorize" button
Select the API Groups from the dropdown and click Subscribe (screenshot)
WIZARD - Run Setup Wizard:

Tuya has changed their data center regions. Make sure you are using the latest version of TinyTuya (v1.2.10 or newer).
From your Linux/Mac/Win PC run the TinyTuya Setup Wizard to fetch the Local_Keys for all of your registered devices:
python -m tinytuya wizard   # use -nocolor for non-ANSI-color terminals
The Wizard will prompt you for the API ID key, API Secret, API Region (cn, us, us-e, eu, eu-w, or in) from your Tuya IoT project as set in Step 3 above.
To find those again, go to iot.tuya.com, choose your project and click Overview
API Key: Access ID/Client ID
API Secret: Access Secret/Client Secret
It will also ask for a sample Device ID. Use one from step 2 above or found in the Device List on your Tuya IoT project.
The Wizard will poll the Tuya IoT Cloud Platform and print a JSON list of all your registered devices with the "name", "id" and "key" of your registered device(s). The "key"s in this list are the Devices' Local_Key you will use to access your device.
In addition to displaying the list of devices, Wizard will create a local file devices.json that TinyTuya will use to provide additional details for scan results from tinytuya.deviceScan() or when running python -m tinytuya scan. The wizard also creates a local file tuya-raw.json that contains the entire payload from Tuya Cloud.
The Wizard will ask if you want to poll all the devices. If you do, it will display the status of all devices on record and create a snapshot.json file with these results.


As you can see more actions can be added to the actions dictionary (work in progress)
# To do: 
## group the lightbulbs by room and add separator to menu
## find a way for the script to differentiate between lighbulbs and other tuya enabled devices.
