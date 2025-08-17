from subprocess import run
from time import sleep as wait
import os

class Macos:
    def __init__(self):
        self.main()

    @staticmethod
    def next_page():
        for i in range(100):
            print()

    def start(self):
        self.next_page()
        print('第一步：拖入要打包的py文件')
        py=' '+input()

        print('第二步：输入打包的py文件库名(没有输入n)')
        imp=input()

        if imp=='n':
            imp=''

        else:
            imp=' --hidden-import '+imp

        print('第三步：拖入资源文件在py程序下的目录(没有输入n)')
        resc=input()

        if resc=='n':
            resc=''

        else:
            resc=' --add-data '+resc+':'+resc

        print('第四步：是否生成单个文件？(输入y或n)')
        io=input()

        if io=='y':
            io_io=' --onefile '

        else:
            io_io=''

        print('第五步：输入文件名')
        name = ' --name '+input()

        set=' --distpath='+os.path.dirname(os.path.realpath(__file__))+'/dist --workpath='+os.path.dirname(os.path.realpath(__file__))+'/build --specpath='+os.path.dirname(os.path.realpath(__file__))+'/build/spec '

        print('请稍后...')

        command=run('pyinstaller '+io_io+name+imp+resc+set+py,shell=True,capture_output=True,text=True)

        if 'Build complete! The results are available in:'in command.stderr:
            print('成功！')

        if 'Error'in command.stderr or'error'in command.stderr or'ERROR'in command.stderr:
            print('失败！')

        print('是否输出终端内容？(输入y或n)')
        abc = bool(input())

        if abc:
            print(command.stdout+command.stderr)
            wait(5)

        self.main()

    def ins_upd(self):
        self.next_page()
        install=run('pip3 install pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple',shell=True,capture_output=True,text=True)

        if 'Successfully installed ' in install.stdout:
            print("安装库成功！")
            wait(3)

        elif 'Requirement already satisfied:' in install.stdout:
            pass

        else:
            print("错误！")
            wait(3)
            quit()

        update = run('pip3 install --upgrade pyinstaller -i https://pypi.tuna.tsinghua.edu.cn/simple', shell=True,capture_output=True, text=True)

        if 'Successfully installed ' in update.stdout:
            print("更新成功！")
            wait(3)

        elif 'Requirement already satisfied:' in update.stdout:
            print('已是最新版！')
            wait(3)

        else:
            print("错误！")
            wait(3)
            quit()

    def main(self):
        self.ins_upd()

        print('欢迎使用Pyinstaller By JIAXING汉化版！')
        print('使用前请仔细阅读github简介(README.md)！')
        print()
        print('##########################################')
        print()
        print('直接回车以开始')
        print('输入q以退出')
        print()
        print('输入你的操作：')
        command=input()

        if command == 'q':
            quit()

        elif command == '':
            self.start()

        else:
            print('无效的操作。。。')
            self.main()

class Windows:
    def __init__(self):
        self.main()

    @staticmethod
    def next_page():
        for i in range(100):
            print()

    def start(self):
        self.next_page()
        print('Windows默认使用auto_py_to_exe图形化工具，正在打开...')
        print('右上角Language调为中文~')
        print('请不要关闭此窗口！')
        os.system('autopytoexe')
        self.main()


    def ins_upd(self):
        self.next_page()

        install=run('pip3 install pyinstaller auto_py_to_exe -i https://pypi.tuna.tsinghua.edu.cn/simple',shell=True,capture_output=True,text=True)

        if 'Successfully installed ' in install.stdout:
            print("安装库成功！")
            wait(3)

        elif 'Requirement already satisfied:' in install.stdout:
            pass

        else:
            print("错误！")
            print(install.stdout+install.stderr)
            wait(3)
            quit()

        update = run('pip3 install --upgrade pyinstaller auto_py_to_exe -i https://pypi.tuna.tsinghua.edu.cn/simple', shell=True,capture_output=True, text=True)

        if 'Successfully installed ' in update.stdout:
            print("更新成功！")
            wait(3)

        elif 'Requirement already satisfied:' in update.stdout:
            print('已是最新版！')
            wait(3)

        else:
            print("错误！")
            wait(3)
            quit()

    def main(self):
        self.ins_upd()

        print('欢迎使用Pyinstaller By JIAXING汉化版！')
        print('使用前请仔细阅读github简介(README.md)！')
        print()
        print('##########################################')
        print()
        print('直接回车以开始')
        print('输入q以退出')
        print()
        print('输入你的操作：')
        command=input()

        if command == 'q':
            quit()

        elif command == '':
            self.start()

        else:
            print('无效的操作。。。')
            self.main()

if __name__ == '__main__'and os.name == 'nt':
    Windows()

else:
    Macos()