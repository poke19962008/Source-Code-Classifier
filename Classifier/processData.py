import os, shutil

def process(path, ext):
    for root, dirs, files in os.walk("./data", topdown=False):
        for name in files:
            if name.split('.')[-1] == ext:
                shutil.move(os.path.join(root, name), os.path.join('./data/%s'%ext, name))



if __name__ == '__main__':
    process('./data/python_dump', 'py')
