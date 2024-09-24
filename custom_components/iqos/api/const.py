# POSSIBLE_WRITE_CHARACTERISTIC_UUIDS = {
#     "SCP_CONTROL_POINT": "e16c6e20-b041-11e4-a4c3-0002a5d5c51b",
#     "FW_UPGRADE_CONTROL": "fe272aa0-b041-11e4-87cb-0002a5d5c51b",
# }
# POSSIBLE_READ_CHARACTERISTIC_UUIDS = {
#     "RRP_SERVICE": "DAEBB240-B041-11E4-9E45-0002A5D5C51B",
#     "DEVICE_BATTERY_CHAR": "f8a54120-b041-11e4-9be7-0002a5d5c51b",
#     "DEVICE_STATUS_CHAR": "ecdfa4c0-b041-11e4-8b67-0002a5d5c51b",
#     "UNKNOWN1": "0aff6f80-b042-11e4-9b66-0002a5d5c51b",
#     "UNKNOWN2": "04941060-b042-11e4-8bf6-0002a5d5c51b",
#     "FW_UPGRADE_STATUS": "15c32c40-b042-11e4-a643-0002a5d5c51b",
# }

CHARACTERISTIC_NOTIFY = "f8a54120-b041-11e4-9be7-0002a5d5c51b"

frame_start = b"(\x07|\x0f)\x00"
frame_case_battery = b"(?P<case_battery>.)"
frame_unknown = b"(?P<unknown>...)"
frame_pen_battery = b"(?P<pen_battery>.?)"

frame_regex = frame_start + frame_case_battery + frame_unknown + frame_pen_battery
