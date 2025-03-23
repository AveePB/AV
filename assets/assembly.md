# Assembly (step by step)

## Table of contents
1. [Introduction](#introduction)
2. [Electronic components](#electronic-components)
3. [Chassis assembly](#chassis-assembly)
4. [Car assembly](#car-assembly)
5. [Raspberry pinout](#pi-pinout)

## Introduction <a name="introduction"></a>
The assembly process should be easy to follow. This guide is an universal standard for construction of AVs. List of components is required to meet criteria, as is the pinout. The only thing, that can differ is the placement of electronic components.

## Electronic Components <a name="electronic-components"></a>
| Image                                   | Component Name     | Quantity |
|-----------------------------------------|--------------------|----------|
| <img src="imgs/raspberry-pi.png" width="100" /> | Raspberry Pi 5 | 1 |
| <img src="imgs/raspberry-pi-ups.png" width="100" /> | Raspberry Pi 5 UPS | 1 |
| <img src="imgs/raspberry-pi-camera.png" width="100" /> | Raspberry Pi Camera HD v3 12MPx | 1 |
| <img src="imgs/rplidar.png" width="100" /> | RPLidar A1M8 | 1 |
| <img src="imgs/18650-battery-holder.png" width="100" /> | 18650 battery holder (3 slots) | 1 |
| <img src="imgs/18650-battery.png" width="100" /> | 18650 battery | 5 |
| <img src="imgs/l298n.png" width="100" /> | L298N motor driver | 2 |
| <img src="imgs/dc-motor.png" width="100" /> | DC motor 6V (48 : 1) | 4 |
| <img src="imgs/jumper-wires.png" width="100" /> | Jumper wires female to female | 1 (set) |

## Chassis Assembly <a name="chassis-assembly"></a>
<img src="./imgs/chassis.png" width="400">

### Recommendation
In this project we have used the <a href="https://botland.com.pl/podwozia-robotow/23563-robot-chassis-mp-zestaw-inteligentnego-podwozia-robota-z-amortyzacja-mecanum-wheels-waveshare-24420.html">chassis</a> from Waveshare.

### L298N chassis tuning
<img src="./imgs/chassis-tuning.png" width="300"><br>
Drill 8 holes in the chassis to mount two l298n controllers. You need to do this in order to have proper mount of l298ns.

## Car Assembly <a name="car-assembly"></a>
...

## Raspberry Pinout <a name="pi-pinout"></a>
<img src="imgs/pi-pinout.png" width="600">

<p>
Check out <a href="https://botland.com.pl/blog/l298n-dwukanalowy-sterownik-silnikow-modul-12v-2-szczegoly-na-temat-produktu-i-przyklady-zastosowan/?cd=15425572033&ad=125523543810&kd=&gad_source=1&gclid=Cj0KCQjw4v6-BhDuARIsALprm33G4zrMTh47Ht2u4vm5Ru8ythna1aj7WtAmzYULeZFdXO5AjWesa70aAsoLEALw_wcB">l298n</a>.
</p>

### Description
- ⬛: *Ground*;
- ⬜: *ENA* controls the speed of left wheel;
- 🌫️: *IN1* spins the left motor forward;
- 🟪: *IN2* spins the left motor backward;
- 🟦: *IN3* spins the right motor forward;
- 🟩: *IN4* spins the right motor backward;
- 🟨: *ENB* controls the speed of right wheel;
