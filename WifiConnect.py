import winwifi

wifiInfo = winwifi.WinWiFi()
wifiAPInfo = winwifi.WiFiAp()


def connectToLocalDroneWifi(accessPointName) -> None:
    print('')
    print(f'Attempting Connection to wifi: {accessPointName}...')
    wifiInfo.connect(accessPointName)
    if getConnectedSSIDName():
        print(f'Connected to {getConnectedSSIDName()}')
    else:
        print('Could not connect to drone wifi')


def getConnectedSSIDName():
    ssidName = ''
    for interface in wifiInfo.get_connected_interfaces():
        ssidName = interface.ssid
    return ssidName

# 'TELLO-626C1C'
