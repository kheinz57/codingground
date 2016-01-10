FILTER=''.join([chr(x)  if x >= 0x20 and x <= 127  else '.' for x in range(256)])
#print FILTER

def dump(src, length=8):
    N=0; result=''
    while src:
       s,src = src[:length],src[length:]
       hexa = ' '.join(["%02X"%ord(x) for x in s])
       s = s.translate(FILTER)
#       print s
       result += "%04X   %-*s   %s\n" % (N, length*3, hexa, s)
       N+=length
    return result

def hexdump(src, length=8):
    result = []
    for i in xrange(0, len(src), length):
       s = src[i:i+length]
       hexa = b' '.join(["%02X" % ord(x)  for x in s])
       text = b''.join([x if 0x20 <= ord(x) < 0x7F else b'.'  for x in s])
       result.append( b"%04X   %-*s   %s" % (i, length*3, hexa, text) )
    return b'\n'.join(result)

with  open('main.py') as f:
#    print dump(f.read(),32)
    hexdump(f.read(),32)
        
