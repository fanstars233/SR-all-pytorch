# super-resolution(2018)

处理为YCbCr形式，仅对亮度通道进行超分，效果不佳，已弃用（2022.11.1）

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

**2022.10.31**

对原始代码进行修改：

1. 将训练和验证图像缩小四倍作为测试
2. 读取和保存模型位置更换，不同模型不同模型名称
3. 预训练模型代码

<img src="https://s2.loli.net/2022/10/31/3VMkbFtlnqrQcvs.jpg" alt="157055_" style="zoom: 200%;" /><img src="https://s2.loli.net/2022/10/31/fdJ3OTCSK4epBU1.jpg" alt="157055" style="zoom:50%;" />



FSRCNN,epoch = 200,当epoch==10时的指标，验证预训练模型的可行性，模型预训练是成功的

![image-20221031193204446](https://s2.loli.net/2022/10/31/s9Yncu7FJUiE5Ha.png)

epoch==200时的指标，中间有些训练过程出现错误，应该是初始lr太大导致的问题

![image-20221031194618782](https://s2.loli.net/2022/10/31/rdSlB7Joifhj9aQ.png)

![157055_fsrcnn](https://s2.loli.net/2022/10/31/FY27TUDhyLkMOXK.jpg)

重新开始训练，lr从0.01改为0.002，epoch=20

![image-20221031201011930](https://s2.loli.net/2022/10/31/h9K3MJZojA6Gx5u.png)

![157055_fsrcnn](https://s2.loli.net/2022/10/31/p8W4qhbAtcaBnum.jpg)

虽然效果也一般但是至少正常了

------

**开正式训练，epoch=100**

1. SRCNN

![image-20221031215321143](https://s2.loli.net/2022/10/31/OsqE9DayGoNYmAi.png)

![157055_srcnn](https://s2.loli.net/2022/10/31/e1LWUXs3CraZ4E9.jpg)

2. FSRCNN

![image-20221031221009067](https://s2.loli.net/2022/10/31/28txIk3nu1ezwpc.png)

![157055_fsrcnn](https://s2.loli.net/2022/10/31/L3EymOCT5MfuBIv.jpg)

3. Subpixcel

![image-20221031221429995](https://s2.loli.net/2022/10/31/Sved42Qb5iMXz7O.png)

![157055_sub](https://s2.loli.net/2022/10/31/jsxOUniJoNISDt3.jpg)

4. VDSR

![Snipaste_2022-11-01_00-12-41](https://s2.loli.net/2022/11/01/sKrgZSykTJjfphb.png)

![157055_vdsr](https://s2.loli.net/2022/11/01/3shXBLTKyaWdofp.jpg)

5. DRCN

![image-20221101110218358](https://s2.loli.net/2022/11/01/FWwk7hRS4jY3zZe.png)

![157055_drcn](https://s2.loli.net/2022/11/01/579LnTShuPU3RZd.jpg)

6. SRGAN

![image-20221101143901197](https://s2.loli.net/2022/11/01/MkOPxLJz4ney5Eg.png)

![157055_srgan](https://s2.loli.net/2022/11/01/lYwG6biIUhQjecz.jpg)

7. EDSR

![image-20221101145318537](https://s2.loli.net/2022/11/01/yIKfs7iL9BaSUZ3.png)

![157055_edsr](https://s2.loli.net/2022/11/01/lqKZ5OuCN4wVMgf.jpg)

8. DBPN



**2022.11.1**

1. 修改测试程序，vdsr和drcn正常运行
2. 保存最优模型



