from time import sleep_ms
from ASL5600L import ASL5600L



myPos = ASL5600L(hyst=1)

print(myPos.getStatus())

while True:
    print('Degrees:', myPos.getAngleDegrees())
    sleep_ms(333)


