import setuptools  # 导入setuptools打包工具


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="love_rimi",  # 用自己的名替换其中的YOUR_USERNAME_
    version="0.0.0.1",  # 包版本号，便于维护版本,保证每次发布都是版本都是唯一的
    author="Sandmeyer",  # 作者，可以写自己的姓名
    author_email="sandmx.work@gmail.com",  # 作者联系方式，可写自己的邮箱地址
    description="A package used to describe love between Rimi and Sandmeyer",  # 包的简述
    long_description=long_description,  # 包的详细介绍，一般在README.md文件内
    long_description_content_type="text/markdown",
    url="https://github.com/SandmX/love_rimi",  # 自己项目地址，比如github的项目地址
    packages=setuptools.find_packages(),
    package_data={'love_rimi': ['this_un/lang/*']},
    entry_points={
        "console_scripts" : ['love_rimi = love_rimi.manage:main']
    }, #安装成功后，在命令行输入mwjApiTest 就相当于执行了mwjApiTest.manage.py中的run了
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',  # 对python的最低版本要求
)
