def cmd_to_ioctl(cmd):
   direction_mask =       0xC0000000
   size_mask      =       0x3FFF0000
   type_mask      =       0x0000FF00
   number_mask    =       0x000000FF

   direction_prefix = "_IO"
   direction_values = ["R", "W", "WR"]

   number = cmd & number_mask
   cmd_type = (cmd & type_mask) >> 8
   size = (cmd & size_mask) >> 16
   direction = (cmd & direction_mask) >> 30

   result = direction_prefix + direction_values[direction-1] + "(\'" + chr(cmd_type) + "\', " + str(number) +  ",  " +  str(size) + ")"
   return result

print "Enter the value as an unsigned integer: "
val = raw_input()
print cmd_to_ioctl(int(val))
