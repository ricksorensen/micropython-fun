## Simple Timing checks ##

Timings using two simple test scripts.  The hardware configuration is:
  
  * Display Hardware: 240x320 2.2" ST7789 display, SPI
  * MCUs:
    * XIAO ESP32C3
	* XIAO RP2400

Two different drivers are tested.

  * st7789_mpy: compiled into firmware and does not use `framebuf`.  This driver writes to display over SPI with every drawing function call (`line`, `rect`, ...)

     <https://github.com/russhughes/st7789_mpy>
  * micropython-nano-gui: uses `framebuf`.  This driver only writes to display when `show` is called, and writes the entire `framebuf`.  
  
     <https://github.com/peterhinch/micropython-nano-gui>
	 
     For the C3 at this time `viper` is not part of the release, so  two varieties are used.  One without `viper` and one with based on a pending pull request.  All other MCU drivers use `viper` mode.
	 
 

Test scripts are:
  
  * `timelines.py` simply draw lines across full screen. 
  * `boxlines.py` randomly place boxes and lines on display.  There are two varieties of this for the `micropython-nano-gui` driver
    * `show` when each drawing loop finishes
	* `show` only at end of all drawing loops

The scripts vary slightly for different drivers due to different setup requirements and APIs.  All runs were done with:

`mpremote mount . exec "import timelines as tod;tod.dorun(5,mcu='rp2',cfg='viper')"`
  
replacing the `mcu` and `cfg` args as needed.  

| test | mcu | driver | opts | s/iter | memuse |
| :---  | --- | -----  | ---  | ----- | ---- |
| timelines | c3 | st7789 |            | 17.21322  | 0     |
| boxlines  | c3 | st7789 |            | 15.18462  | 0     |
| boxlines  | c3 | nano   | viper_end  | 0.2975246 | 38560 |
| timelines | c3 | nano   | viper      | 0.1444348 | 38560 |
| boxlines  | c3 | nano   | viper_loop | 76.87507  | 40240 |
| boxlines  | c3 | nano   | _end       | 3.259891  | 48512 |
| timelines | c3 | nano   |            | 3.106737  | 52000 |
| [^1]boxlines | c3 | nano | _loop | 3024.658 | 9872 |
| timelines | rp2 | nano | viper | 0.229179 | 38560 |
| boxlines | rp2 | nano | viper_loop | 67.1678 | 106752 |
| boxlines | rp2 | nano | viper_end | 0.528 | 38560 |
| timelines | rp2 | st7789 |  | 1.183125 | 0 |
| boxlines | rp2 | st7789 |  | 2.767351 | 0 |
[^1]: Only 1 iteration used for C3 non-viper boxlines due to runtime. 
