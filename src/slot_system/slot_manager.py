class SlotManager:
    def __init__(self):
        self.slots = {}
        self.dependencies = {}
    
    def register_slot(self, slot):
        """注册槽位到管理器"""
        self.slots[slot.name] = slot
    
    def add_dependency(self, main_slot, depends_on):
        """添加槽位依赖关系"""
        if main_slot not in self.dependencies:
            self.dependencies[main_slot] = []
        self.dependencies[main_slot].extend(depends_on)
    
    def validate_slot(self, slot_name, value):
        """验证槽位值是否符合规则"""
        slot = self.slots.get(slot_name)
        if not slot:
            raise ValueError(f"未知槽位: {slot_name}")
        
        # 类型验证
        if slot.type == "int":
            if not isinstance(value, int):
                return False, "需为整数"
                
            # 范围检查
            if "min" in slot.attributes and value < slot.attributes["min"]:
                return False, f"不能小于{slot.attributes['min']}"
            if "max" in slot.attributes and value > slot.attributes["max"]:
                return False, f"不能大于{slot.attributes['max']}"
        
        elif slot.type == "enum":
            if value not in slot.attributes.get("options", []):
                return False, f"无效选项，有效值: {slot.attributes['options']}"
        
        return True, "验证通过"
    
    def check_dependencies(self, slot_name):
        """检查依赖是否满足"""
        required = self.dependencies.get(slot_name, [])
        missing = [s for s in required if not self.slots.get(s).value]
        return not bool(missing), missing
