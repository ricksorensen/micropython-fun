Simple programs to experiment with sending binary data over micropython REPL.

- `chkbytes.py`: demonstrate sending int array, string, bytes out REPL with `print` and `sys.stdout`
- `fakerepltmit.py`: send binary data via REPL- arbitrary, for evaluation
- `readfake.py`: read binary data from (linux) serial port and disply

See https://docs.micropython.org/en/latest/library/io.html?highlight=buffer for a discussion on io streams and buffering.  micropython does not implement buffered io internally.  While in CPython `stdout.write(str)` takes (only) a string argument and `stdout.buffer.write(bytes)` take only a byte iterable, micropython versions take either, and the SAMD21 port does not have a `stdout.buffer` option.
