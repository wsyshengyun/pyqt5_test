#  Copyright (c) 2023. Lorem ipsum dolor sit amet, consectetur adipiscing elit.
#  Morbi non lorem porttitor neque feugiat blandit. Ut vitae ipsum eget quam lacinia accumsan.
#  Etiam sed turpis ac ipsum condimentum fringilla. Maecenas magna.
#  Proin dapibus sapien vel ante. Aliquam erat volutpat. Pellentesque sagittis ligula eget metus.
#  Vestibulum commodo. Ut rhoncus gravida arcu.

# coding:utf8

from ..pack.config import Json, path, JsonSetPc, JsonIpOnline
import pytest
@pytest.mark.skip(reason='some')
def test_pack_config():
    assert Json.is_path_exist(path)
    value = {'a':1, 'b':2, 'c':3, 'd': [1,2,3,4,5]}
    value1 = {"a":1, "b":2, "c":3, "d": [1,2,3,4,5]}
    assert value == value1
    obj = Json()
    obj.set(value)
    obj.write()
    
    val = obj.read()
    assert val == value

# @pytest.mark.skip(reason='some')
def test_json_setips():
    data = [['192.168.65.152', '192.168.44.215', '192.168.7.151', '192.168.0.152'], ['255.255.255.0', '255.255.255.0', '255.255.255.0', '255.255.255.0'], 'Microsoft KM-TEST 环回适配器']
    name ='pcips'
    setpc = JsonSetPc()
    # print(setpc.obj)
    setpc.set(data)
    assert data == setpc.get()
    
    
# -------------------------------------------------------------
# ip_on_line test
# -------------------------------------------------------------
def test_online_config():
    online = JsonIpOnline()
    try:
        online.get_value('ip', 'start_end1')
        assert 1 == 1
    except KeyError:
        assert 0 == 1
    
    online.add_section('ip', 'start_end1', ['3', '5'])
    online.add_section('ip', 'start_end2', ['6', '7'])

