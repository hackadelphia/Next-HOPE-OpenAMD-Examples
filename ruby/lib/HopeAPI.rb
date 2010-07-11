require 'uri'
require 'cgi'
require 'rubygems'
require 'curb'

module HopeAPI
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

  def self.get_full_uri(type)
    # XXX cheating!
    URI.parse([FEED_URI, 'api', type].join('/') + '/')
  end

  def self.make_request(type, *args)
    uri  = get_full_uri(type)
    # XXX totally broken for dupe keys, but meh. Ruby's HTTP clients blow.
    args = (args[0] || { }) rescue { } 
    uri.query = args.keys.map { |key| CGI.escape("#{key}=#{argv[0][key]}") }.join(';')

    body = Curl::Easy.http_get(uri.to_s)
    return body.body_str
  end
end

if __FILE__ == $0
  puts HopeAPI.make_request('location')
end
