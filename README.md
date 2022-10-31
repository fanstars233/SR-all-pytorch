# super-resolution(2018)
A collection of super-resolution models & algorithms

Detail introduction of each model is in corresponding sub-folds.

Authored by [icpm](https://github.com/icpm)

## Requirement
- python3.6
- numpy
- pytorch 1.0.0

## Models
- [VDSR](https://github.com/icpm/super-resolution/tree/master/VDSR)
- [EDSR](https://github.com/icpm/super-resolution/tree/master/EDSR)
- [DCRN](https://github.com/icpm/super-resolution/tree/master/DRCN)
- [SubPixelCNN](https://github.com/icpm/super-resolution/tree/master/SubPixelCNN)
- [SRCNN](https://github.com/icpm/super-resolution/tree/master/SRCNN)
- [FSRCNN](https://github.com/icpm/super-resolution/tree/master/FSRCNN)
- [SRGAN](https://github.com/icpm/super-resolution/tree/master/SRGAN)
- [DBPN](https://github.com/icpm/super-resolution/tree/master/DBPN)

## Usage
train:

```bash
$ python3 main.py -m [sub/srcnn/cdsr/edsr/fsrcnn/drcn/srgan/dbpn]
```

super resolve:

```bash
$ python3 super_resolve
```



## Train_log

对原始代码进行修改：

1. 将训练和验证图像缩小四倍作为测试
2. 读取和保存模型位置更换，不同模型不同模型名称
3. 预训练模型代码

2022.10.31

FSRCNN,epoch = 200,当epoch==10时的指标，验证预训练模型的可行性

![image-20221031193204446](https://s2.loli.net/2022/10/31/s9Yncu7FJUiE5Ha.png)

epoch==200时的指标，中间有些训练过程错误

![image-20221031194618782](https://s2.loli.net/2022/10/31/rdSlB7Joifhj9aQ.png)

![157055_fsrcnn](https://s2.loli.net/2022/10/31/FY27TUDhyLkMOXK.jpg)

应该初始lr太大导致的问题