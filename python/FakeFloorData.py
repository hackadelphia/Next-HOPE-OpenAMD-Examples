


#data from http://wiki.hope.net/images/1/10/TNH_mezzanine_layout.jpg
#data in pixels for now, to convert to meters at approx 65 px = 3.66 meters

#data in Meters
floor_data =  [
{
    "name" : "Hammock Zone",
    # at px 0,0 size 354x76
    "vertices": [[0.0, 0.0],[51.58,0.0],[15.58,3.65],[0.0,3.65]],
    "floor": 1
    "acces":"public"
},
{
    "name" : "Low Power Zone",
	#at px 0,76  until 54 x (85)
    "vertices": [[0.0, 3.65],[15.58,3.65],[15.58,7.27],[0.0,7.24]],
    "floor": 1
    "acces":"public"
},
{
    "name" : "untitled 1",
    # at px 450,76  size 63, 56
    "vertices": [[19.81, 3.65],[22.76,3.65],[22.76,6.24],[19.81,6.24]],
    "floor": 1
    "acces":"public"
},
{
    "name" : "Art Space 2",
	# at px 0,162  size 152,90
    "vertices": [[0.0, 7.24],[15.58,7.24],[15.58,10.74],[0.0,10.74]],
    "floor": 1,
    "acces":"public"
},
{
    "name" : "Interview Area",
    #at px 0,234 size 82, 90
    "vertices": [[0.0, 10.74],[4.34,10.74],[4.34,13.96],[0.0,13.96]],
    "floor": 1,
    "acces":"limited"
}
{
    "name" : "Keynote Bullpen",
	# at px 0, 326 size 82,147
    "vertices": [[0.0, 13.96],[4.34,13.96],[4.34,13.96],[0.0,=13.96]],
    "floor": 1,
    "acces":"limited"
}
	'name' : "stairs",
 	#at px 82, 250 sz 266, 139
    "vertices": [[0.0, 13.96],[4.34,13.96],[4.34,13.96],[0.0,=13.96]],
    "floor": 1,
    "acces":"public",
 	
]

#"NOC" at 84,414 size 188,52
#"Core Staff Area" at 88,462 size 180,132
#"NOC NOC" at 273, 513 size 15,24
#"Security Center" at 273, 513 size 98,140
#"AMD Work Area" at 0,590 size 178,65
#"AV Stream Work Area" at 65,590 size 90,70
#"Ethernet Tables" at 0, 658 size 175,75 
#Project Telephread" at 175,658 size 110, 80
#Art Space 1" at 0, 736, points at (736, 352), (736 + 255, 352),
#	(736 + 255, 80) (736+ 85, 80), (736+ 85, 0)

#"Segway Track" at 0, 821 points at (80,821), (80, 821 + 170), 352, 994),
#(588, 990) (598, 1067), (0,1067)

#"Info Desk" at 368, 732 size 92,82
#"Volunteer Lounge" at 453, 746 size 139,73
#"Radio Statler" at 363, 816 size 94,88
#"Radio/News Work Area" at 460,816 size 132, 124

#"Walkway" at 0, 354, points at (0, 510) 75,512 75,447 
#638, 445 638,640 330,640 330,700 723,700 723,292 660, 292 660,360

#"Vendor Tables" at 330, 440  size 316,200 
