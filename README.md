# PodAndGitUpdate
自动更新当前目录及子目录下所有的pod仓库和git仓库(默认为脚本所在目录)

```shell
 _____  _  _           ______             _   _   _             _         _         
|  __ \(_)| |    ___   | ___ \           | | | | | |           | |       | |        
| |  \/ _ | |_  ( _ )  | |_/ /  ___    __| | | | | | _ __    __| |  __ _ | |_   ___ 
| | __ | || __| / _ \/\|  __/  / _ \  / _` | | | | || '_ \  / _` | / _` || __| / _ \\
| |_\ \| || |_ | (_>  <| |    | (_) || (_| | | |_| || |_) || (_| || (_| || |_ |  __/
 \____/|_| \__| \___/\/\_|     \___/  \__,_|  \___/ | .__/  \__,_| \__,_| \__| \___|
                                                    | |                             
                                                    |_|                             
        
```

# 背景
最近开发采用了组件化，导致一个项目中有很多仓库，仓库的更新和`pod update`浪费很多时间，所以开发了这个脚本，帮助减少耗时。

# 依赖
`python3.0` 及以上

# 使用方法
```shell
python Update_Git_Pod.py
```

# 参数及介绍
>`-h`或`--help`,展示帮助

>`-g`或`--git`,只更新git仓库

>`-p`或`--pod`,只更新pod仓库

>`-d`或`--dir`,指定根目录，用法:`-d=[newPath]`或`--dir=[newPath]`
