require 'rubygems'
require 'uri'
require 'cgi'
require 'curb'
require 'json'

module HopeAPI
  FEED_URI = "http://api.hope.net"
  
  # various feed structs
  Speaker  = Struct.new(:name, :bio)
  Location = Struct.new(:area, :time, :x, :y, :user, :button)
  Talk     = Struct.new(:speakers, :title, :abstract, :time, :track, :interests)
  User     = Struct.new(:name, :x, :y, :interests)

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

  #
  # args are the GET parameters. use the force.
  #
  def self.make_request(type, args={})
    uri  = get_full_uri(type)
    # XXX totally broken for dupe keys, but meh. Ruby's HTTP clients blow.
    uri.query = args.keys.map { |key| CGI.escape("#{key}=#{args[key]}") }.join(';')

    resp = Curl::Easy.http_get(uri.to_s)

    unless resp.response_code == 200
      raise "Response #{resp.response_code} received"
    end

    # API improperly yields text/plain, so we run with that case.
    unless resp.content_type == "text/plain" or resp.content_type == "application/json"
      raise "Invalid content type: #{resp.content_type}"
    end

    return JSON.load(resp.body_str)
  end

  # see above
  def self.to_ruby(type, args={ })
    type = type.to_s

    data = make_request(type, args)

    # special case for interests
    return data if type == 'interests' 

    # XXX moar cheating
    const_type = type.gsub(/s$/, '')
    struct_klass = const_get(const_type.capitalize)

    raise "not a valid type" unless struct_klass

    results = []
   
    if type == "users" or type == "speakers" 
      data = data.map { |x| x[1] }
    end

    data.each do |item|
      s = struct_klass.new
      item.keys.each do |key|
        s[key] = item[key]
      end

      results.push(s)
    end

    return results
  end
end

if __FILE__ == $0
  %w[
    locations
    interests
    users
    speakers
    talks
  ].each do |type|
    p HopeAPI.to_ruby(type)
  end
end
