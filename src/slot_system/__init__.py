# src/slot_system/__init__.py

# -------------------------------
# 模块说明：
# 该 __init__.py 文件用于初始化 slot_system 模块，显式暴露对外接口。
# 主要职责是聚合和统一导出 slot_system 子模块中的核心类和函数。
# 这样，使用者只需从 slot_system 导入需要的组件，而不必关心其具体定义在哪个子模块中。
# -------------------------------

# 从 slot_structure 模块导入核心槽位类和槽位创建函数
from .slot_structure import Slot, create_travel_slots

# 从 slot_manager 模块导入槽位管理器
from .slot_manager import SlotManager

# 定义模块公开接口，用于控制 from slot_system import * 时能导入的对象
__all__ = [
    'Slot',                 # 槽位类，用于描述单个信息槽的结构和属性
    'create_travel_slots',  # 工厂函数，用于批量创建特定类型（如旅游类）的槽位集合
    'SlotManager'           # 槽位管理器类，负责槽位的状态更新、完整性检查等操作
]
