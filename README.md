# PixStamp

> [![hugo-papermod](https://img.shields.io/badge/PixStamp-By_Yellow--BringtEast-red)](https://github.com/Yellow-BringtEast/PixStamp)
> [![download](https://img.shields.io/github/downloads/Yellow-BringtEast/PixStamp/total.svg)](https://github.com/Yellow-BringtEast/PixStamp/releases)
> [![license](https://img.shields.io/github/license/Yellow-BringtEast/PixStamp)](https://github.com/Yellow-BringtEast/PixStamp/blob/master/LICENSE)
> ![language](https://img.shields.io/github/languages/top/Yellow-BringtEast/PixStamp?color=orange)
>
> **这是一个基于PySide6开发的用于添加exif水印的桌面工具。**
---
# 项目结构
```
PixStamp/                 # 项目根目录
│   
├── LICENSE                       # 许可证书
├── main.py                       # 程序主入口
├── README.md                     # 项目说明文件
├── requirements.txt              # Python依赖文件
├── assets/                       # 资源文件夹
│   ├── fonts/                    # 字体文件
│   └── logos/                    # 相机品牌logos
├── src/                          # 源代码文件夹
│   ├── exceptions.py             # 异常类
│   ├── controllers/              # 控制器文件夹，处理应用逻辑
│   ├── models/                   # 模型文件夹，管理数据和业务逻辑
│   ├── utils                     # 工具文件夹，存放工具函数和实用模块
└── ui/                           # 界面设计和布局文件夹
```
---
# 功能介绍
## 1、界面展示
![界面展示.png](assets%2Fmd_pic%2F%E7%95%8C%E9%9D%A2%E5%B1%95%E7%A4%BA.png)

## 2、功能演示
### 2.1 导入照片
#### 2.1.1 导入单个照片
![打开文件.gif](assets%2Fmd_pic%2F%E6%89%93%E5%BC%80%E6%96%87%E4%BB%B6.gif)

#### 2.1.2 导入多个照片
![打开多个文件.gif](assets%2Fmd_pic%2F%E6%89%93%E5%BC%80%E5%A4%9A%E4%B8%AA%E6%96%87%E4%BB%B6.gif)

#### 2.1.3 导入文件夹
![打开文件夹.gif](assets%2Fmd_pic%2F%E6%89%93%E5%BC%80%E6%96%87%E4%BB%B6%E5%A4%B9.gif)

### 2.2 处理照片
#### 2.2.1 处理当前照片
![处理当前图片.gif](assets%2Fmd_pic%2F%E5%A4%84%E7%90%86%E5%BD%93%E5%89%8D%E5%9B%BE%E7%89%87.gif)

#### 2.2.2 处理全部照片
![处理全部图片.gif](assets%2Fmd_pic%2F%E5%A4%84%E7%90%86%E5%85%A8%E9%83%A8%E5%9B%BE%E7%89%87.gif)

### 2.3 保存照片
#### 2.3.1 保存当前照片
![保存当前照片.gif](assets%2Fmd_pic%2F%E4%BF%9D%E5%AD%98%E5%BD%93%E5%89%8D%E7%85%A7%E7%89%87.gif)

#### 2.3.3 保存全部照片
![保存全部照片.gif](assets%2Fmd_pic%2F%E4%BF%9D%E5%AD%98%E5%85%A8%E9%83%A8%E7%85%A7%E7%89%87.gif)

---
# TODO
- [x] 文件保存功能
- [ ] 菜单栏-更多弹窗功能
- [ ] exif信息编辑
- [ ] 更多水印样式
- [ ] 界面美化
- [ ] 项目打包为exe文件

# 特别感谢
Semi-Utils: https://github.com/leslievan/semi-utils
