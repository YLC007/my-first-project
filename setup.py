# 导入 setuptools 包，它是 Python 官方推荐的打包工具
# setup 用于配置项目的元信息和安装方式
# find_packages 是一个帮助函数，用来自动查找项目中的所有 Python 包（含 __init__.py 的目录）
from setuptools import setup, find_packages

# 调用 setup() 函数，配置你的项目（包）的基本信息和安装规则
setup(
    name="slot_system",  # 项目的名称。安装后别人可以通过 import slot_system 来使用这个包
    version="0.1.0",      # 项目的版本号，格式通常为 主版本号.次版本号.修订号。建议每次发布新版本时更新

    # 自动查找项目中所有的包（文件夹中含有 __init__.py 的都会被认为是包）
    # 这里限定只在 "src" 目录下查找，而不是在根目录查找
    packages=find_packages(where="src"),

    # 指定包的实际代码目录是 "src"
    # 意思是：虽然安装后的包名是 slot_system，但代码文件在 src/slot_system/ 中
    package_dir={"": "src"},
)
