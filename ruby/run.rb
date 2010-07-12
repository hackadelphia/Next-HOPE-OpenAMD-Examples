require 'rubygems'
require 'sinatra'
require 'haml'
require 'lib/hopeapi'

get '/' do
  haml :index
end

#
# api/locations/?user=12345 # => type = 'location'; params = {:user => 12345}
#
get '/api/:type/' do
  type = params[:type]
  args = params.reject {|key, val| key == :type }
  content_type :json
  HopeAPI.make_request(type, args).to_json
end
