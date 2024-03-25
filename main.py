import win32com.client
x=0
wmi = win32com.client.GetObject("winmgmts:")
for usb in wmi.ExecQuery("SELECT * FROM Win32_PnPEntity WHERE Caption LIKE '%USB%'"):
    try:
        print("Name:", usb.Name)
        print("DeviceID:", usb.DeviceID)
        print()
        x+=1
    except Exception as e:
        print(f"Error accessing properties: {e}")


print(x)

x=r"""


Name: Périphérique d’entrée USB
DeviceID: USB\VID_3434&PID_0313&MI_01\6&30B99A73&0&0001 ####

Name: Périphérique d’entrée USB
DeviceID: USB\VID_3434&PID_0313&MI_02\6&30B99A73&0&0002 ####

Name: Périphérique d’entrée USB
DeviceID: USB\VID_093A&PID_2521\5&3B8EB818&0&1

Name: Périphérique d’entrée USB
DeviceID: USB\VID_3434&PID_0313&MI_00\6&30B99A73&0&0000 ####

Name: Périphérique USB composite
DeviceID: USB\VID_0408&PID_5321\0X0001

Name: Périphérique USB composite
DeviceID: USB\VID_3434&PID_0313\5&3B8EB818&0&2 ####

Name: Hub USB racine (USB 3.0)
DeviceID: USB\ROOT_HUB30\4&8CA4CD4&0&0

Name: Hub USB racine (USB 3.0)
DeviceID: USB\ROOT_HUB30\1&2B53A856&0&0

Name: Contrôleur hôte Intel(R) USB 3.1 eXtensible - 1.10 (Microsoft)
DeviceID: PCI\VEN_8086&DEV_9DED&SUBSYS_8532103C&REV_30\3&11583659&0&A0

Name: Parsec Virtual USB Adapter
DeviceID: ROOT\USB\0000



Name: Périphérique USB composite
DeviceID: USB\VID_3434&PID_0313\5&3B8EB818&0&2

Name: Périphérique d’entrée USB
DeviceID: USB\VID_3434&PID_0313&MI_01\6&30B99A73&0&0001

Name: Périphérique d’entrée USB
DeviceID: USB\VID_3434&PID_0313&MI_02\6&30B99A73&0&0002

Name: Hub USB racine (USB 3.0)
DeviceID: USB\ROOT_HUB30\4&8CA4CD4&0&0

Name: Hub USB racine (USB 3.0)
DeviceID: USB\ROOT_HUB30\1&2B53A856&0&0

Name: Contrôleur hôte Intel(R) USB 3.1 eXtensible - 1.10 (Microsoft)
DeviceID: PCI\VEN_8086&DEV_9DED&SUBSYS_8532103C&REV_30\3&11583659&0&A0

Name: Parsec Virtual USB Adapter
DeviceID: ROOT\USB\0000

Name: Périphérique d’entrée USB
DeviceID: USB\VID_3434&PID_0313&MI_00\6&30B99A73&0&0000

Name: Périphérique USB composite
DeviceID: USB\VID_0408&PID_5321\0X0001
"""