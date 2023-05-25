import sys

d = [0x41, 0x42, 0x0D, 0x0A]  # 'AB\r\n'
db = bytes(d)
print("d:  int array, human readable")
print(d)
print("db: bytes array, human readable")
print(db)

print("db: bytes array, raw")
nw = sys.stdout.buffer.write(db)  # returns number written
print("| done {}\n\n".format(nw))

print("db: bytes array, raw, one at time")
# note on bytes
#   bytes(n)   ... n an integer, returns a null array of length n
#   bytes(str) ... str a string/iterable return an encoded array of len(str)
for i in range(len(d)):
    _ = sys.stdout.buffer.write(bytes([d[i]]))  # or bytes(d[i:i+1])
print("| done {}\n\n".format(nw))
