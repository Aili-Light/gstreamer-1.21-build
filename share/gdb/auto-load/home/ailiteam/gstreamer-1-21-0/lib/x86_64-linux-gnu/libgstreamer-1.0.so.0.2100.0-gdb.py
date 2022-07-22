import sys
import gdb

# Update module path.
dir_ = '/home/ailiteam/gstreamer-1-21-0/share/gstreamer-1.0/gdb'
if not dir_ in sys.path:
    sys.path.insert(0, dir_)

from gst_gdb import register
register (gdb.current_objfile ())
