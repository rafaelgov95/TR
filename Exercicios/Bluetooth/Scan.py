from bluetooth import *
server_sock=BluetoothSocket(RFCOMM )


print "performing inquiry..."

nearby_devices = discover_devices(lookup_names = True)

print "found %d devices" % len(nearby_devices)

for name, addr in nearby_devices:
     print " %s - %s" % (addr, name)

port = 1
bd_addr = "48:5A:B6:F5:70:94"

sock=BluetoothSocket( RFCOMM )
sock.connect((bd_addr, port))

sock.send("hello!!")