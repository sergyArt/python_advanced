from subprocess import *
std_out=Popen(['ping','-c','1', 'yandex.ru'], stdout=PIPE)
for line in std_out.stdout:
    line=line.decode('cp866').encode('utf-8')
    print(line.decode('utf-8'))
