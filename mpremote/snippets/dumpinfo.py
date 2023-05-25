# print machine, memory, filesystem, modules information
import gc
import micropython
import sys
import machine
import os

knownmcu = False
try:
    import samd as mcu

    knownmcu = True
except:
    try:
        import rp2 as mcu

        knownmcu = True
    except:
        try:
            import esp32 as mcu

            knownmcu = True
        except:
            try:
                import nrf as mcu

                knownmcu = True
            except:
                print("no mcu module found")

print("gc_free: {}".format(gc.mem_free()))  # older/smaller do not allow f-string
gc.collect()
print("gc_free: {}".format(gc.mem_free()))
micropython.mem_info()

print("--- Sys Info ---")
# sys.path
# sys.path.append("/lib")
print("  platform:       ", sys.platform)
print("  version:        ", sys.version)
print("  implementation: ", sys.implementation)
print("  path:           ", sys.path)
try:
    print("  unique_id:      ", machine.unique_id())
except:
    print("  unique_id:      Not Available")
print("--- Modules ---")
help("modules")
print("    dir(machine)")
print(dir(machine))
if knownmcu:
    print("    dir(mcu)")
    print(dir(mcu))
    if "esp32" in sys.platform:
        import esp

        print("    dir(esp)")
        print(dir(esp))
        del esp
else:
    print("    unknown MCU")
# returns: blocksize, fragmentsize, nblocks (*fragmentsize)
#          nfree blocks, blkavail,
#          ninodes, nfree inodes,
#          navail inodes, mountflgs, maxfnamelength
fsstats = os.statvfs("/")
print(
    "\n--- FileSyst: Size={}   Free={}".format(
        fsstats[0] * fsstats[2], fsstats[0] * fsstats[3]
    )
)
# check a file/directory
#  0: file type
#  1: inode (???)
#  2: device(???)
#  3: num hard links (???)
#  4: owner
#  5: group
#  6: file size
#  7,8,9: mod time
# stat = os.stat('/')
print("gc_free: {}".format(gc.mem_free()))
del machine, sys, micropython, mcu, os
gc.collect()
print("gc_free: {}".format(gc.mem_free()))
