require 'rubygems'
require 'sinatra'
require 'haml'
require 'lib/hopeapi'

get '/' do
  haml :index
end

##
# api/locations/?user=12345 # => type = 'location'; params = {:user => 12345}
##
get '/api/:type/' do
  content_type :json
  HopeAPI.make_request(params[:type], params.reject {|key, val| key == :type } ).to_json
end
