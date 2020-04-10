import subprocess
import sys
import re

def get_current_process(filename):
    with open(filename, 'w+') as f:
        ps = subprocess.run(['ps','-u','muhamed'], stdout=f, stderr=subprocess.DEVNULL)

def check_browser_running(fname):
    get_current_process(fname)
    a="browser is not working"
    with open(fname) as f:
        for i in f:
            p1=re.compile('^.*chrome.*$|^.*firefox.*$')
            if p1.match(i):
                a="browser is working"
            
    return a


def main():
    a=check_browser_running(sys.argv[1])
    print(a)

if __name__ == "__main__":
    main()
