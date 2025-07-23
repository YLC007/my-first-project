class Slot:
    def __init__(self, name, slot_type, parent=None):
        self.name = name
        self.type = slot_type
        self.parent = parent
        self.children = []
        self.attributes = {}

    def add_child(self, child_slot):
        """添加子槽位"""
        child_slot.parent = self
        self.children.append(child_slot)

    def set_attribute(self, key, value):
        """设置槽位属性"""
        self.attributes[key] = value


# 预定义旅游领域核心槽位
def create_travel_slots():
    # 主槽位
    destination = Slot("目的地", "str")
    time_frame = Slot("时间", "time_range")
    budget = Slot("预算", "int")
    travel_type = Slot("旅行类型", "enum")

    # 预算子槽位
    currency = Slot("货币单位", "enum", budget)
    per_person = Slot("人均预算", "int", budget)
    budget.add_child(currency)
    budget.add_child(per_person)

    # 旅行类型子槽位
    activity = Slot("活动类型", "enum", travel_type)
    group_size = Slot("团队规模", "int", travel_type)
    travel_type.add_child(activity)
    travel_type.add_child(group_size)

    return [destination, time_frame, budget, travel_type]