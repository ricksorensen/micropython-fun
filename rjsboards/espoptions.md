Here are options for GENERIC builds.

default value from mpconfigport.h
module values from boards/ESP32_GENERIC_xx/mpconfigboard.h

| option | default | ESP32 | C2 | C3 | C6 | S2 | S3 |
| --- | --- | --- | --- | --- | --- | --- | --- |
| MICROPY_HW_ENABLE_SDCARD | 1 | | 0 |
| MICROPY_PY_MACHINE_I2S | SOC_I2S_SUPPORTED | | 0 | | 0 |
| MICROPY_HW_ENABLE_UART_REPL | (!MICROPY_HW_USB_CDC && !MICROPY_HW_ESP_USB_SERIAL_JTAG) | | | 1 | 1 | 1 | 1 |
| MICROPY_PY_BLUETOOTH | 1 | | | | | 0 |
| MICROPY_PY_ESPNOW | 1 |
| MICROPY_PY_MACHINE_I2C_TARGET | (SOC_I2C_SUPPORT_SLAVE &&!CONFIG_IDF_TARGET_ESP32 && !CONFIG_IDF_TARGET_ESP32C6) |
| MICROPY_PY_MACHINE_DAC | (SOC_DAC_SUPPORTED) |
 
SOC_I2C_SUPPORT_SLAVE = 1

SOC_I2S_SUPPORTED = 1

SOC_DAC_SUPPORTED = 1 ESP32, ESP32S2

SOC_USB_OTG_SUPPORTED=1 ESP32S2,S3,P4

SOC_USB_SERIAL_JTAG_SUPPORTED = 1 C3,C6,S3

MICROPY_HW_USB_CDC <- MICROPY_HW_ENABLE_USBDEV <- SOC_USB_OTG_SUPPORTED       S2,S3

MICROPY_HW_ESP_USB_SERIAL_JTAG <- (SOC_USB_SERIAL_JTAG_SUPPORTED && !MICROPY_HW_USB_CDC)   

ESP module options from espidf/components/soc include directories using IDF V5.4.2 on 20250825, searching for SOC_xxxx_SUPPORTED settings.

| option          | esp32 | c2 | c3 | c5 | c6 | s2 | s3 | p4 |
|:----------------|:-----:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
| ADC             | 1     | 1  | 1  | 1  | 1  | 1  | 1  | 1  |
| DAC             | 1     | -  | -  | -  | -  | 1  | -  | -  |
| UART            | 1     | 1  | 1  | 1  | 1  | 1  | 1  | 1  |
| BT              | 1     | 1  | 1  | 1  | 1  | -  | 1  | -  |
| BTE             | -     | -  | -  | -  | -  | -  | -  | -  |
| WIFI            | 1     | 1  | 1  | 1  | 1  | 1  | 1  | -  |
| ULP             | 1     | -  | -  | 1  | 1  | 1  | 1  | 1  |
| I2S             | 1     | -  | 1  | 1  | 1  | 1  | 1  | 1  |
| RMT             | 1     | -  | 1  | 1  | 1  | 1  | 1  | 1  |
| I2C             | 1     | 1  | 1  | 1  | 1  | 1  | 1  | 1  |
| I2C_SLAVE       | 1     | -  | 1  | 1  | 1  | 1  | 1  | 1  |
| WDT             | 1     | 1  | 1  | 1  | 1  | 1  | 1  | 1  |
| BLE             | 1     | 1  | 1  | 1  | 1  | -  | 1  | -  |
| BT_CLASSIC      | 1     | -  | -  | -  | -  | -  | -  | -  |
| PCNT            | 1     | -  | -  | 1  | 1  | 1  | 1  | 1  |
| RNG             | 1     | 1  | 1  | 1  | 1  | 1  | 1  | 1  |
| USB_OTG         | -     | -  | -  | -  | -  | 1  | 1  | 1  |
| USB_SERIAL_JTAG | -     | -  | 1  | 1  | 1  | -  | 1  | 1  |
