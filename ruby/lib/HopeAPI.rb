class HopeAPI
  FEED_URI = "http://api.hope.net"
  
  # various feed structs
  Speaker  = Struct.new(:name, :bio)
  Location = Struct.new(:area, :time, :x, :y, :user, :button)
  Talk     = Struct.new(:speakers, :title, :abstract, :time, :track, :interests)
  Profile  = Struct.new(:name, :x, :y, :interests)

  # TODO worth it to enumerate?
  INTERESTS = [ 
    "tech", 
    "activism", 
    "radio", 
    "lockpicking", 
    "crypto", 
    "privacy", 
    "ethics", 
    "telephones", 
    "social engineering", 
    "hacker spaces", 
    "hardware hacking", 
    "nostalgia", 
    "communities", 
    "science", 
    "government", 
    "network security", 
    "malicious software", 
    "pen testing", 
    "web", 
    "niche hacks", 
    "media" 
  ]
end
