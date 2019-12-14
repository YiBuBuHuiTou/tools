#######################################################################################
#
#                            高德Web API 共通调用方法
#  [history]                        [reason]                   [date]        
#  DNST_coldchain_pre               new                        2019年12月12日
#
#######################################################################################
require 'uri'
require 'net/http'
require 'net/https'
require 'json'

module Amap

    class AmapService 

        # 高德地图API key
        # TODO   => 配置文件
        Amap_key = 'b2a293d97bd3bb280b27e01516460eef'

        # 初期化函数    api名     api 参数        api类型           地理围栏id
        def initialize(api_name = nil, options = nil, api_type = 'GET', gid = nil)
            @api_name = api_name if !api_name.nil?
            if !options.nil? && options.is_a?(Hash)
                @options = options
            end
            @api_type = api_type
            @gid = gid
            @uri = self.generate_uri
            @request = self.generate_request
        end

        # 高德API base url （http）
        def amap_base_url
            'https://restapi.amap.com/'
        end

        # 高德API url(POST + GET)
        def ampap_api_url
            api_url = self.amap_base_url
            case @api_name
            # 地理编码
            when 'geo'
                api_url += "v3/geocode/geo?output=json&key=#{Amap_key}"
            # 逆地理编码
            when 'regeo'
                api_url += "v3/geocode/regeo?output=json&key=#{Amap_key}"
            # 坐标转换
            when 'convert'
                api_url += "v3/assistant/coordinate/convert?output=json&key=#{Amap_key}"
            # 货车路径规划
            when 'truck'
                api_url += "v4/direction/truck?key=#{Amap_key}"
            # 测距
            when 'distance'
                api_url += "v3/distance?output=json&key=#{Amap_key}"
            # 搜索POI 按范围搜索
            when 'around'
                api_url += "v3/place/around?output=json&key=#{Amap_key}"
            # 批量处理
            when 'batch'
                api_url += "v3/batch?key=#{Amap_key}"

            # 创建地理围栏/查询围栏 API  POST/GET
            when 'geofence_meta'
                api_url += "v4/geofence/meta?key=#{Amap_key}"

            # 更新地理围栏 API POST
            when 'geofence_update'
                api_url += "v4/geofence/meta?key=#{Amap_key}&gid=#{@gid}&method=patch"
            # 删除围栏
            when 'geofence_delete'
                api_url += "v4/geofence/meta?key=#{Amap_key}&gid=#{gid}&method=delete"
            # 围栏监控
            when 'geofence_status'
                api_url += "v4/geofence/status?key=#{Amap_key}"

            else
                # 不支持的api
                raise "unknown api name : #{@api_name}"
            end
            api_url
        end

        # GET请求生成parameter字符串
        def options2s
            params = ""
            if @api_type == "GET"
                @options.each { |key, value|
                    if value.is_a?(Array)
                        a2s = value.to_s
                        params += "&#{key}=#{a2s[1,a2s.length-1]}"
                    else
                        params += "&#{key}=#{value}"
                    end
                }
            else 
                raise "this method just for 'GET' , no support for #{@api_type}"
            end
            puts params
            params
        end

        # 生成uri
        def generate_uri
            uri = nil
            if @api_type == "GET"
                 if @options.nil?
                    uri = URI(self.ampap_api_url)
                 else 
                    uri = URI(URI.escape(self.ampap_api_url + self.options2s))
                 end
            elsif @api_type == "POST"
                uri = URI(self.ampap_api_url)
            else
                raise "not supported request type :#{@api_type}"
            end
            uri
        end

        def generate_request
            request = nil
            if @uri.nil?
                return request
            end
            if @api_type == "GET"
                request = Net::HTTP::Get.new(@uri)
            else @api_type == "POST"
                request = Net::HTTP::Post.new(@uri)
                if !@options.nil?
                    request.set_form_data(@options)
                end
            end
            request
        end
        # 发送API请求
        def send_request
        puts @uri.to_s
            result = nil
            if @uri.scheme == "http"
                result = Net::HTTP.start(@uri.host, @uri.port, :open_timeout => 60, :read_timeout => 60) do |http|
                    http.request(@request)
                end
            else
                result = Net::HTTP.start(@uri.host, @uri.port, :use_ssl =>true, :verify_mode => OpenSSL::SSL::VERIFY_NONE, :open_timeout => 10, :read_timeout => 10) do |http|
                    http.request(@request)
                end
            end
            return result.body if !result.nil?
        end
    end
    opt = Hash.new
    opt[:location] = [116.481488,39.990464]
    puts AmapService.new('regeo',opt).send_request
    
end