Board List

	* XIAO SAMD21- use `micropython/port/samd/boards/SEEED_XIAO_SAMD21`
	* XIAO NRF52- use `micropython/port/nrf/boards/SEEED_XIAO_NRF52`
	* SEEED WIO Terminal (SAMD51)- use `micropython/port/samd/boards/SEEED_WIO_TERMINAL`
    * XIAO RP2040-use `rjsboards/SEEED_XIAO_RP2040`
	  LED is different than default PICO board
	* RPI PICOW- use `micropython/port/rp2/boards/RPI_PICO_W`
	* RPI PICO2- use `micropython/port/rp2/boards/RPI_PICO2`
	* RPI PICO2 RISCV- use `micropython/port/rp2/boards/RPI_PICO2` with variant `RISCV`
	* XIAO ESP32C3
		Highly dependent on Espressif IDF version
	* XIAO ESP32S3
		Highly dependent on Espressif IDF version
	
RJSBoards

SEEED_XIAO_SAMD21VFS

+ add support for FATFS for use with SD cards.

SEEED_XIAO_RP2040

+ add XIAO specific PIN names and change LED pin.

SEEED_XIAO_ESPSML2   COMPRESS OFF        too big
ESP32_GENERIC_S3       COMPRESS OFF
SEEED_XIAO_ESP32C3    COMPRESS DEF       okay
SEEED_XIAO_ESPSMLFS   COMPRESS OFF     too big
SEEED_XIAO_ESP32S3X/SEEED_XIAO_ESP32S3     COMPRESS DEF    too big
+ original was ESP32_GENERIC_S3          COMPRESS DEF            too big  no ulab, no sd
+ no variant, only SPIRAM_OCT load config used
+ cmake includes SPIRAM_OCT parameters
+ xiao sdkconfig sets XIAO strings and NORESET?
+ adds pins.csv file


SEEED_XIAO_ESP32C3:
+ original was ESP32_GENERIC_C3
+ do not enable ESP SDCard
+ add default SCL/SDA pins to build
+ add pins.csv file

SEEED_XIAO_ESPSML
+ reduce size by including fewer modules
+ specify manifest.py only asyncio networking onewire umqtt
    no aioespnow, dht, ds18x20,neopixel, upysh

SEEED_XIAO_ESPSMLFS
+ reduce size of local FS to give more room for build.
   + specify partitions and new sdkconfig

SEEED_XIAO_C3SMALL
+ same as ESP32C3???

SEEED_XIAO_ESP32C3SD
+ enable ESP SD Card

SEEED_XIAO_ESPSML2
+ reduce size by including fewer modules
+ specify manifest.py only asyncio networking
    no aioespnow, dht, ds18x20,neopixel, upysh,mqtt,onewire



ESP32C3:

mpconfigboard.h:

+ allow I2S
+ UART_REPL config still evaluating

add pins.csv with I2C, SPI, UART pins ad D0-D10,A0-A10



ESP32S3:

mpconfigboard.cmake:
   8MB Flash, OCT-SPIRAM, 240MHz

mpconfigboard.h:
   specify I2C0 pins
   
add pins.csv with I2C, SPI, UART pins ad D0-D10,A0-A10



RP2040
mpconfigboard.cmake:
  specify PICO_BOARD as "seeed_xiao_rp2040" to use RP2 SDK defines for this 
  
mpconfigboard.h:
  change LED Pin to GPIO17
  
SAMD21 same ...

ESPSML:
manifest.py
mpconfigboard.cmake:
  add FROZEN_MANIFEST specification
mpconfigboard.h:

+ allow I2S
+ UART_REPL config still evaluating

ESPSMLFS:
mpconfigboard.cmake: 
   use sdkconfig.small.board with larger app partition leaving smaller vfs
   
sdkconfig.small.board, partitions-smallfs.csv for repatitioning flash


# ESP32C3 Generic Builds #
| version | compiler | binsize | fs size | gc_free |
|---|---|---|---|---|
| v1.19.1 | 4.4.1 | 1431808 | 2084864 | 120224 |
| v1.20.0 | 4.4.3 | 1461232 | 2084864 | 130080 |
| v1.21.0 | 5.0.2 | 1587840 | 2084864 | 207632 |
| v1.22.2 | 5.0.4 | 1664208 | 2084864 | 199440 |
| v1.23.0 | 5.0.4 | 1667600 | 2084864 | 199440 |
| v1.24.1 | 5.2.2 | 1779264 | 2084864 | 174864 |
| v1.25.0 | 5.2.2 | 1835856 | 2084864 | 174912 |
| v1.26.0prvw | 5.4.1 | 1879408 | 2084864 | 174880 |


| board | build | binsize | operation | notes |
|-------|-------|----------|-----------|-------|
|  nrf | ulab, framebuf, ssd1306, st7789      | 788480 | boots, dumpinfo  |       |
|  samd21 | framebuf, ssd1306, select       | 390656 | boots, dumpinfo |       |
|  wio |       | 840704 |           |       |
|  pico |       |          |           |       |
|  picow | ulab, framebuf, neopixel, ssd1306, st7789       | 2010624         | boots, dumpinfo           |       |
|  xiaorp2 |       | 985600         | boots, dumpinfo, i2s  | some difficulty with first connection  |
|  pico2 |       | 943616          |           |       |
|  pico2riscv |       | 1161216          |           |       |
|  unix | ulab, framebuf, btree       | 1063368         | starts, dumpinfo          |       |
| xiaoc3 |       |1873248          |           |       |
| xiaos3x | ulab, framebuf, ssd1306, st7780, mqtt, neopixel, ntptime       | 2029536          | boots, dumpinfo, holiday |       |
| gens3 |       |2029232          |           |       |
|       |       |          |           |       |
