# IQOS Heated Tobaco for Home Assistant
This project is an attempt at getting IQOS integrated into Home Assistant, most of this code was based on [LD2410](https://github.com/home-assistant/core/tree/dev/homeassistant/components/ld2410_ble) integration by [930913](https://github.com/930913)

I wanted to have a way to track and keep tabs on my consumption with home assistant and set up alerts when i am overdoing it.

The design of IQOS bluetooth is not ideal, it was made mostly to allow firmware updates to the device with only a back tought into making it usable for tracking information.

# Main features
* Checking the battery of the IQOS charger
* Know and set alerts when the IQOS pen is fully charged (on devices that have separate pen/case)
* Tracking when the IQOS pen is removed and inserted in the case, very useful to know your usage.

# Installation instructions

1. The esiest way to install the integration is using HACS. Just click the
   button bellow and follow the instructions:
   [![Open your Home Assistant instance and open a repository inside the Home Assistant Community Store.](https://my.home-assistant.io/badges/hacs_repository.svg)](https://my.home-assistant.io/redirect/hacs_repository/?owner=megarushing&repository=ha-iqos) 

   Alternatively, you can go to HACS and: 

- a) Click on the 3 dots in the top right corner.
- b) Select "Custom repositories"
- c) Add the URL to this repository: https://github.com/megarushing/ha-iqos.
- d) Select integration.
- e) Click the "ADD" button.

2. Now turn off your IQOS device by holding the power button for 5 seconds until all lights go off.
3. Turn on your device by holding the power button again for 5 seconds. When the device boots, it boots in pairing mode.
4. Navigate to Settings -> Devices & Services, the IQOS device should be auto-detected.
 
   If its not detected, go to Settings -> Devices & Services in Home Assistant and click the "Add Integration" button. Search for "IQOS" and install it. Your device should appear in the list, if it doesn't, try steps 2 and 3 again.
5. A screen will appear with a submit button to install the device, please make sure it was freshly booted (steps 2 & 3) BEFORE clicking submit
6. Patiently wait, IQOS takes some time to get connected first time.

# Known Issues
1. Instead of using bluetooth passwords IQOS only broadcasts during the first minutes of boot, this means that if your device disconnects, you might need to turn it off and on again for it to be able to connect once more, very annoying.
2. When using multiple bluetooth proxies the bluetooth connection is not handed over between them, instead the device loses connection and fails to connect to the next proxy. Device will also need a reboot at that time to be able to connect again.

### Enabling debug logging
* Add the following to your configuration.yaml file then restart HA:
  ```
  logger:
    default: warn
    logs:
      custom_components.iqos: debug

# Legal Notice
This integration is not built, maintained, provided or associated with IQOS or Philip Morris in any way.
