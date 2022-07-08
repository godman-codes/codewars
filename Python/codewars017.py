def int32_to_ip(int32):
   # first_number = int32//16777216
   # second_number = (int32%16777216)//65536
   # third_number = ((int32%16777216)%65536)//256
   # last_number = ((int32%16777216)%65536)%256
   return f'{int32//16777216}.{(int32%16777216)//65536}.{((int32%16777216)%65536)//256}.{((int32%16777216)%65536)%256}'


print(int32_to_ip(2154959208))
print(int32_to_ip(0))
print(int32_to_ip(2149583361))