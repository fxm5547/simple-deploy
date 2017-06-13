## Simple deploy tool
- This is a simple operation tool wrote by Python and based on pssh and git;
- The tool function includes project full deploy or update, command excute, and file sync.

### Reference
- [A Byte of Python](http://www.cuhk.edu.cn/library/dw/tg/il/Python_shen.pdf)
- [pssh manual](https://www.mankier.com/1/pssh)
- [pscp manual](https://www.mankier.com/1/pscp)
- [pssh blog](https://ruiaylin.github.io/2014/11/20/pssh/)

### Usage Introduction for macOS
- install pssh：`brew install wget && wget https://storage.googleapis.com/google-code-archive-downloads/v2/code.google.com/parallel-ssh/pssh-2.3.1.tar.gz && tar zxvf pssh-2.3.1.tar.gz && cd pssh-2.3.1 && python setup.py install`
- [config login servers through SSH Public Key](https://www.digitalocean.com/community/tutorials/how-to-configure-ssh-key-based-authentication-on-a-linux-server)
- excute `python main.py`

### onfiguration
- under config dir;
- in config/config.py: add/modify projects, commands and files;
- in config/ssh_hosts.txt: add/modify hosts for projects deploying and command eccuting;
- in config/scp_hosts.txt: add/modify hosts for file sync.

### Screen capture
![screen capture](./files/imgs/deploy.png)