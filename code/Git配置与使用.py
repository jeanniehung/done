"""
git的配置：
一：注册github
二：下载最新的git
三：进入终端
    1：git--version：查看git的版本号
    2：cd～/.ssh:进入到ssh目录
    3:ls:查看ssh目录下的内容
    4：rm -rf ia_rsa id_rsa.pub:删除这两个文件，为配置ssh密钥作准备
#第5第6步是在干什么呢？
    5：touch config————》vim config————》输入：
            Host github.com
            User 注册github用的邮箱
            Hostname ssh.github.com
            PreferredAuthentications publickey
            IdentityFile ~/.ssh/id_rsa
            Port 443
    6：ssh -T git@github.com————》输入yes
    7：cd ..
       ssh-keygen -t rsa-C"注册git邮箱"：一路回车（不要在ssh目录下执行该操作）
    8；cd ~/.ssh————》ls:会出现ia_rsa id_rsa.pub
       cat id_rsa.pub:会出现一串内容，copy
四：浏览器登陆github
    1：光标移动到头像位置————》点击setting（设置）
    2：点击SSH and GPC keys（ssh和GPG密钥）
    3：标题：ssh_keys
       键：第三步第六小步copy的内容粘贴进去
五：打开你要的把内容放进去的仓库
    1：点击clone or download（克隆或下载）
    2：点击Use SSH
    3：copy那段内容
       eg；git@github.com:jeanniehung/learning_python.git
六：进入终端
    1：进入一个你储存代码的目录
    2：git clone 第五步第三小步copy的内容（下载仓库的内容到该目录下）
#配置内容还差什么姐姐你补充一下8
git的使用：
一：打开pycharm
    1：点击open
    2：选择git配置第六步第1步选择的目录
二：在该目录下新建一个文件（会有弹窗提示）（假设为test.py）
    1:代码输入完毕
    2：点击最上面工具栏VCS————》Git————》Commit file
        a：勾选你要上传到仓库的文件（test.py）
        b：输入该文件的标签，点击commit
    3：点击最上面工具栏VCS————》Git————》push（等待上传）
        右下方出现成功提醒，文件已经上传到仓库
    4：点击最上面工具栏VCS————》Git————》pull
        可以查看仓库的最新内容
"""