 # -*- coding: UTF-8 -*-
require 'csv'


#---------------------------------------------
# 文件头不读取， 如果要读取文件第一行 把：headers => true 删掉
# csv 行 第一列为 * ， - 或空 也不读取
#-----------------------------------------------
def parse_csv(file)
    raw_data = Array.new
    begin
        if not File::exist?(file) 
            raise File::basename(file) + "： 文件不存在"
        end
        if not File::readable?(file)
            raise File::basename(file) + ": 文件不可读"
        end
        CSV.foreach(file, :headers => true) do | row |
            if row.empty? or row[0].nil? or row[0].to_s.strip == '' or row[0].to_s.strip == '*' or row[0].to_s.strip == '-' 
                next
            end
            raw_data << row
        end
        
    rescue Exception => e
        puts e.message
    end
    raw_data
end