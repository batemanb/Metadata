import exifread
# Open image file for reading (binary mode)
f = open("/Users/motiv/Desktop/graphene/20210614/HOPG/topleftcorner.tif", 'rb')

# Return Exif tags
tags = exifread.process_file(f)

# Print the tag/ value pairs
for tag in tags.keys():
    if tag in ('Image Tag 0x877A'):
        #print("Key: %s, value %s" % (tag, tags[tag]))
        test_string=tags[tag]
        x1=float(test_string.printable.split("StageX=")[1].split("\r")[0])
        y1=float(test_string.printable.split("StageY=")[1].split("\r")[0])
        
# Open image file for reading (binary mode)
f = open("/Users/motiv/Desktop/graphene/20210614/HOPG/flake1_after.tif", 'rb')

# Return Exif tags
tags = exifread.process_file(f)

# Print the tag/ value pairs
for tag in tags.keys():
    if tag in ('Image Tag 0x877A'):
        #print("Key: %s, value %s" % (tag, tags[tag]))
        test_string=tags[tag]
        x2=float(test_string.printable.split("StageX=")[1].split("\r")[0])
        y2=float(test_string.printable.split("StageY=")[1].split("\r")[0])
        
delx=x2-x1
dely=y2-y1

print("delta x = %f" % delx)
print("delta y = %f" % dely)