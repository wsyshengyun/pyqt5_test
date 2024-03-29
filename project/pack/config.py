#  Copyright (c) 2022. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8
import os
import json



path = 'project\\config\\setting.json'

class Json(object):
    __instance = None
    
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance =  object.__new__(cls)
        return cls.__instance
        
        
    def __init__(self, path = path):
        
        self.path = path
        self.obj = {}
        
    @classmethod
    def is_path_exist(cls, path):
        import os
        return os.path.exists(path)
    
    def write(self):
        with open(self.path, 'w', encoding='utf8') as f:
            json.dump(self.obj, f)
        
    def read(self):
        with open(self.path, 'r', encoding='utf8') as f:
            value = json.load(f)
            if isinstance(value, dict):
                self.obj = value
            else:
                raise TypeError("读取json文件必须是一个字典")
        return self.obj
    
    def set(self, v):
        if not isinstance(v, dict):
            return
        self.obj = v
        

class JsonSetPc(object):
    def __init__(self):
        
        self.jsonobj = Json()
        self.key = 'pcips'
        self.jsonobj.read()
        self.obj: dict = self.jsonobj.obj
        
        self.obj.setdefault(self.key, [])
        
    
    def get(self):
        return self.obj.get(self.key)
        pass
    
    def set(self, v):
        self.obj[self.key] = v
        self.jsonobj.write()
    
    
class JsonIpOnline(object):
    def __init__(self):
        
        self.json = Json()
        self.key = "ip_on_line"
        self.json.read()
        self.obj:dict = self.json.obj
        self.ips_dict = self.obj.setdefault(self.key, {})
        self.ips_dict.setdefault('ip', {
           "start_end1": [],
           "start_end2": []
        })
        
    def get_value(self, sec, option):
        return self.ips_dict.get(sec).get(option)
        pass
    
    def add_section(self, sec, option=None, value=None):
        if sec not in self.ips_dict:
            self.ips_dict.setdefault(sec, {})
        if option:
            self.ips_dict[sec][option] = value
        self.json.write()
        
    
    
    
        

if __name__ == '__main__':
    pass


