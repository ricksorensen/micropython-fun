"list filesystem information"
import os
import gc


fsstats = os.statvfs("/")
print(
    "--- FileSyst: Size={}   Free={}".format(
        fsstats[0] * fsstats[2], fsstats[0] * fsstats[3]
    )
)
gc.collect()
del os, gc
