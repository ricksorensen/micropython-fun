// This configuration is for a generic ESP32C3 board with 4MiB (or more) of flash.

#define MICROPY_HW_BOARD_NAME               "XIAOC3"
#define MICROPY_HW_MCU_NAME                 "ESP32C3"

#define MICROPY_HW_ENABLE_SDCARD            (0)

// Enable UART REPL for modules that have an external USB-UART and don't use native USB.
//   Results in 600 bytes bigger, and still noisy first connect after hw reset
//#define MICROPY_HW_ENABLE_UART_REPL         (1)
