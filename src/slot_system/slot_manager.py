class SlotManager:
    def __init__(self):
        # 槽位注册表：保存所有注册过的槽位对象，键为槽位名称
        self.slots = {}

        # 槽位依赖表：记录某个槽位依赖哪些其他槽位（用于后续的完整性检查）
        self.dependencies = {}

    def register_slot(self, slot):
        """注册一个槽位到管理器中"""
        # 以槽位的名称为键，将槽位对象保存到 self.slots 字典中
        self.slots[slot.name] = slot

    def add_dependency(self, main_slot, depends_on):
        """
        添加槽位依赖关系
        main_slot：主槽位名
        depends_on：列表，表示主槽位依赖的其他槽位名称
        """
        if main_slot not in self.dependencies:
            self.dependencies[main_slot] = []
        # 将依赖项追加到该槽位的依赖列表中
        self.dependencies[main_slot].extend(depends_on)

    def check_slot(self, slot_name, value):
        """
        验证某个槽位的值是否有效
        参数：
            slot_name：要验证的槽位名称
            value：要验证的值
        返回：
            (是否有效, 说明信息)
        """
        # 获取指定名称的槽位对象
        slot = self.slots.get(slot_name)
        if not slot:
            raise ValueError(f"未知槽位: {slot_name}")
        
        # 类型为整数的验证逻辑
        if slot.type == "int":
            if not isinstance(value, int):
                return False, "需为整数"
                
            # 如果设置了最小值，进行下限检查
            if "min" in slot.attributes and value < slot.attributes["min"]:
                return False, f"不能小于{slot.attributes['min']}"
            # 如果设置了最大值，进行上限检查
            if "max" in slot.attributes and value > slot.attributes["max"]:
                return False, f"不能大于{slot.attributes['max']}"
        
        # 枚举类型验证逻辑
        elif slot.type == "enum":
            # 判断 value 是否在允许的选项列表中
            if value not in slot.attributes.get("options", []):
                return False, f"无效选项，有效值: {slot.attributes['options']}"
        
        # 通过所有检查则认为验证成功
        return True, "验证通过"

    def check_dependencies(self, slot_name):
        """
        检查某个槽位的所有依赖项是否都有值（是否已满足）
        返回：
            (是否满足所有依赖, 未满足的槽位列表)
        """
        # 获取该槽位依赖的所有其他槽位名称
        required = self.dependencies.get(slot_name, [])
        # 找出尚未赋值的槽位
        missing = [s for s in required if not self.slots.get(s).value]
        # 如果 missing 非空，返回 False 和缺失项；否则返回 True
        return not bool(missing), missing
