MCU_SERIES = SAMD21
CMSIS_MCU = SAMD21G18A
LD_FILES = boards/samd21x18a.ld sections.ld
TEXT0 = 0x2000

MICROPY_VFS_FAT ?= 1
SRC_C += \
	fatfs_port.c
