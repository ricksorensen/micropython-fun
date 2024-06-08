Here is information on using a SPI ST7789 display driver as developed by Russ Hughes.  See [https://github.com/russhughes/st7789_mpy](https://github.com/russhughes/st7789_mpy "https://github.com/russhughes/st7789_mpy"). 
When this is compiled as a module into micropython the display is driven quite briskly.

For a pure python implementation see:
[https://github.com/russhughes/st7789py_mpy](https://github.com/russhughes/st7789py_mpy "https://github.com/russhughes/st7789py_mpy")
This is quite a bit slower, but has the same display operations.

Note that this driver can be used fro SPI ILI9341 displays also- see the configuration files for details.

The examples for this driver include a module to define the display and SPI interface parameters.

I have included configurations for various displays and processors based on my simple SPI display testbed.  Processors include:

  * SEEED XIAO RP2040
  * SEEED XIAO ESP32C3
  * SEEED XIAO NRF82541
  * SEEED WIO Terminal
  * UM TINY S3
  
Displays include:

  * ST7789 135x240
  * ST7789 240x320
  * ILI9341 240x320 ( with and without resistive touch)
  * ILI9341 240x320 ( with and without capacitive touch)
  
  
