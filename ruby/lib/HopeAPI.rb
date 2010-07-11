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

  def get_full_uri(type)
    URI.join(FEED_URI, 'api', type)
  end

  def make_request(type, *args)
    req = Net::HTTP::Get.new(get_full_uri(type))
    res = Net::HTTP.new(url.host, url.port).start {|http| http.request(req) }

    case res
    when Net::HTTPSuccess, Net::HTTPRedirection
      return res
    else
      raise res.error!
    end
  end
end
