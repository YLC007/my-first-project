from slot_system.slot_manager import SlotManager
from slot_system.slot_structure import Slot

def test_slot_validation():
    manager = SlotManager()
    
    # 注册带范围的槽位
    budget = Slot("预算", "int")
    budget.set_attribute("min", 100)
    budget.set_attribute("max", 10000)
    manager.register_slot(budget)
    
    # 测试验证
    valid, msg = manager.validate_slot("预算", 5000)
    assert valid is True
    
    valid, msg = manager.validate_slot("预算", 50)
    assert valid is False
    assert "不能小于100" in msg

def test_dependencies():
    manager = SlotManager()
    
    # 注册槽位
    destination = Slot("目的地", "str")
    hotel = Slot("酒店类型", "enum")
    manager.register_slot(destination)
    manager.register_slot(hotel)
    
    # 设置依赖：酒店依赖于目的地
    manager.add_dependency("酒店类型", ["目的地"])
    
    # 测试依赖检查
    destination.value = "北京"
    satisfied, missing = manager.check_dependencies("酒店类型")
    assert satisfied is True
    
    destination.value = None
    satisfied, missing = manager.check_dependencies("酒店类型")
    assert satisfied is False
    assert "目的地" in missing
