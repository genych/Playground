import os
import zipfile as zf
from random import random
import shutil

def uberunzip(source_dir=os.getcwd(), dest_dir=os.getcwd()):
    """ Grabs all zip files from source folder (and subfolders) and extract them to destination, including zips in zips, zips in zips in zips and so on. By default from current to current folder. Be carefull """
    if not os.path.isdir(source_dir) or not os.path.isdir(dest_dir):
        print('source or destination not found')
        return

    tmp = os.path.join(dest_dir, 'tmp_%s' % random())
    os.mkdir(tmp)

    zips = []
    while True:
        for dpath, _, fnames in os.walk(source_dir):
            for fname in fnames:
                fullpath = os.path.join(dpath, fname)
                if zf.is_zipfile(fullpath):
                    zips.append(fullpath)
                    print('found %s' % fullpath)

        if not zips:        # time to move on
            for item in os.listdir(tmp):
                item = os.path.join(tmp, item)
                print('moving %s to %s' % (item, dest_dir))
                shutil.move(item, dest_dir)
            os.rmdir(tmp)
            print('done')
            return

        while zips:
            fullpath = zips.pop()
            # new folder for each .zip (to minimize collisions) in temporary folder replicating original structure. holy crap
            newdir = os.path.splitext(
                        os.path.join(tmp,
                            os.path.relpath(fullpath, start=source_dir)))[0]
            print('extracting to %s' % newdir)
            with zf.ZipFile(fullpath) as file:
                file.extractall(path=newdir)
            os.remove(fullpath)
        source_dir = tmp


if __name__ == '__main__':
    uberunzip()
