import pytest
from slot_system.slot_structure import Slot, create_travel_slots

def test_slot_creation():
    budget = Slot("预算", "int")
    assert budget.name == "预算"
    assert budget.type == "int"
    assert len(budget.children) == 0

def test_nested_slots():
    slots = create_travel_slots()
    budget = next(s for s in slots if s.name == "预算")
    
    assert len(budget.children) == 2
    assert budget.children[0].name == "货币单位"
    assert budget.children[1].parent.name == "预算"

def test_slot_attributes():
    slot = Slot("测试", "int")
    slot.set_attribute("min", 100)
    slot.set_attribute("max", 10000)
    
    assert slot.attributes["min"] == 100
    assert slot.attributes["max"] == 10000
