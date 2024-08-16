import setuptools  # 导入setuptools打包工具
import atexit
import shutil
import os


name = "love_rimi"  # 包名

"""------ 删除打包过程中产生的中间文件 ------"""


def rm_temp():
    """删除打包过程中产生的中间文件"""
    shutil.rmtree('build')
    shutil.rmtree('{}.egg-info'.format(name))


# 注册 rm_temp
atexit.register(rm_temp)

"""------ 读取依赖文件 ------"""

def strip_comments(path):
    """也可以使用读取requirements.txt文件的形式,下面是从
    requirements.txt文件读取依赖列表的常见做法之一："""
    return path.split('#', 1)[0].strip()

def reqs(*f):
    return list(filter(None, [strip_comments(path) for path in open(os.path.join(os.getcwd(), *f)).readlines()]))


"""------ 读取自述文件 ------"""

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


"""------ 开始打包 ------"""

setuptools.setup(
    name=name,  # 包名
    version="0.0.1.3",  # 包版本号，便于维护版本,保证每次发布都是版本都是唯一的
    author="Sandmeyer",  # 作者，可以写自己的姓名
    author_email="sandmx.work@gmail.com",  # 作者联系方式，可写自己的邮箱地址
    description="A package used to describe love between Rimi and Sandmeyer",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://github.com/SandmX/love_rimi",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    install_requires=reqs('requirements.txt'),
    package_data={'love_rimi': ['this_un/lang/*']},
    entry_points={
        "console_scripts": ['love_rimi = love_rimi.manage:main']
    },  # 安装成功后，在命令行输入mwjApiTest 就相当于执行了mwjApiTest.manage.py中的run了
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)
