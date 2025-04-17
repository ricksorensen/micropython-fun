#define MICROPY_HW_BOARD_NAME "Seeed Xiao"
#define MICROPY_HW_MCU_NAME   "SAMD21G18A"

#define MICROPY_HW_XOSC32K  (1)
#define MICROPY_HW_ADC_VREF (2)

#define MICROPY_HW_DEFAULT_UART_ID  (4)
#define MICROPY_HW_DEFAULT_I2C_ID   (2)
#define MICROPY_HW_DEFAULT_SPI_ID   (0)

// see micropython issues
// https://github.com/micropython/micropython/issues/5860
// fatfs configuration used in ffconf.h
#define MICROPY_FATFS_ENABLE_LFN            (1)
#define MICROPY_FATFS_RPATH                 (2)
#define MICROPY_FATFS_MAX_SS                (4096)
#define MICROPY_FATFS_LFN_CODE_PAGE         437 /* 1=SFN/ANSI 437=LFN/U.S.(OEM) */
