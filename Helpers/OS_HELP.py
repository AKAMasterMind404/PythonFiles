import pathlib
from os import listdir, remove, rename
from os.path import isfile, join
import shutil


class OsHelp:
    @staticmethod
    def path():
        return str(pathlib.Path().resolve())

    @staticmethod
    def filesInDirectory(**kwargs):
        _path = kwargs.get("path")
        _path = _path if _path is not None else OsHelp.path()
        return [f for f in listdir(_path) if isfile(join(_path, f))]

    @staticmethod
    def deleteFile(path):
        remove(path)

    @staticmethod
    def deleteFolder(path):
        shutil.rmtree(path)

    @staticmethod
    def rename(path, name):
        p = pathlib.Path(path)
        p.rename(pathlib.Path(p.parent, name))


if __name__ == '__main__':

    path = OsHelp.path()
    fileList = OsHelp.filesInDirectory()

    for file in fileList:
        if file.__contains__(".mp4"):
            if not file.__contains__("-converted"):
                OsHelp.deleteFile(path + f'\{file}')

    for file in fileList:
        if file.__contains__(".mp4"):
            if file.__contains__("-converted"):
                newname = "".join(file.split("-converted"))
                OsHelp.rename(path + f"/{file}", path + f"/{newname}")
