def cmd_to_ioctl(cmd):
   direction_mask =       0b11000000000000000000000000000000
   size_mask      =       0b00111111111111110000000000000000
   type_mask      =       0x0000FF00
   number_mask    =       0x000000FF

   direction_values = "_IORW"

   number = cmd & number_mask
   cmd_type = (cmd & type_mask) >> 8
   size = (cmd & size_mask) >> 16
   direction = (cmd & direction_mask) >> 30

   result = direction_values[:direction+2] + "(\'" + chr(cmd_type) + "\', " + str(number) +  ",  " +  str(size) + ")"
   return result

print "Enter the value as an unsigned integer: "
val = raw_input()
