# -*- coding: utf-8 -*-

# PullAllRepo
# 将目录下所有的git仓库更新到当前分支的最新版本
import sys
import os


def logo():
    print("""
 _____  _  _           ______             _   _   _             _         _         
|  __ \(_)| |    ___   | ___ \           | | | | | |           | |       | |        
| |  \/ _ | |_  ( _ )  | |_/ /  ___    __| | | | | | _ __    __| |  __ _ | |_   ___ 
| | __ | || __| / _ \/\|  __/  / _ \  / _` | | | | || '_ \  / _` | / _` || __| / _ \\
| |_\ \| || |_ | (_>  <| |    | (_) || (_| | | |_| || |_) || (_| || (_| || |_ |  __/
 \____/|_| \__| \___/\/\_|     \___/  \__,_|  \___/ | .__/  \__,_| \__,_| \__| \___|
                                                    | |                             
                                                    |_|                             
                                                                  
    """)

def __help():
    print("此脚本用来帮助批量更新【Git】仓库和【Pod】库。")
    print("请确保git仓库不需要输入【账号】、【密码】或其他配置。")
    print("默认更新脚本所在目录下所有包括子目录的git仓库和pod库。")
    print("注意：1.如果git仓库工作区不干净，默认不更新，请手动更新\n2.`-g` 和 `-p`只有一个参数生效，请勿同时设置\n")
    print("-------------可选参数--------------\n")
    print("参数 `-h` 或 `--help`    查看帮助.")
    print("参数 `-g` 或 `--git`     只更新git仓库")
    print("参数 `-p` 或 `--pod`     只更新pod库")
    print("参数 `-d` 或 `--dir`    指定根目录，用法：\n   `-d=[newPath]` 或者: \n   `--dir=[newPath]`")
    print("-------------------------------\n")

def getInputPath(inputPath):
    # inputPath = str(input("请输入要处理的目录:"))
    print("输入的目录为：" + inputPath)
    if len(inputPath) == 0:
        print("未传入自定义根目录，以脚本当前所在目录为根目录！")
        return os.getcwd()
    else:
        return inputPath

def isGitDirty(path):
    os.system("cd %s"%path)
    return os.system("git diff --quiet") != 0


def listFile(filePath):
    for root, dir, file in os.walk(filePath):
        if ".git" in dir:
            gitRepoPaths.append(root)

        if "Podfile" in file:
            podfilePaths.append(root)


def pullAllGitRepo(paths):
    for path in paths:
        print("--->>> 👉️👉️ 准备更新【Git】仓库：%s" % path)
        os.chdir(path)
        if isGitDirty(path) == True:
            print("--->>> ❌ 【Git】工作区不干净，请手动更新[%s] ❌" % path)
        else:
            os.system("git pull")
    print("---->>>> ✅【Git】仓库更新完成 ✅ <<<<----\n\n")

def updateAllPod(paths):
    for path in paths:
        os.chdir(path)
        print("--->>> 👉️👉️ 准备更新【Pod】库：%s\n"%path)
        os.system("pod update")
    print("---->>>> ✅【Pod】库更新完成 ✅ <<<<----\n\n")


if __name__ == '__main__':

    # 显示简介
    logo()

    # print(sys.argv)

    # 获得帮助
    if ('-h' in sys.argv or '--help' in sys.argv):
        __help()
        exit(0)

    # 初始化变量
    podfilePaths = []
    gitRepoPaths = []
    canUpdateGit = True
    canUpdatePod = True
        
    # 获得用户输入目录
    rootPath = ""

    for tmpArg in sys.argv:
        if ('-d=' in tmpArg):
            rootPath = getInputPath(tmpArg.replace('-d=',''))
            break
        elif ('--dir=' in tmpArg):
            rootPath = getInputPath(tmpArg.replace('--dir=',''))
            break
    
    if len(rootPath) == 0: 
        rootPath = getInputPath("")

    # 遍历目录
    listFile(rootPath)
    # print("git repo paths: %s"%gitRepoPaths)
    # print("-----------\n podfilePaths: %s"%podfilePaths)

    # 判断是否只需要更新git仓库
    if ('-g' in sys.argv or '--git' in sys.argv):
        canUpdateGit = True
        canUpdatePod = False

    # 判断是否只需要更新Pod库
    if ('-p' in sys.argv or '--pod' in sys.argv):
        canUpdatePod = True
        canUpdateGit = False

    if canUpdateGit == True:
        pullAllGitRepo(gitRepoPaths)

    if canUpdatePod == True: 
        updateAllPod(podfilePaths)

    print("✅ 全部处理完成，请查看 ✅")
