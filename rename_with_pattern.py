import easygui , glob, os


def rename(dir, pattern, titlePattern):
    for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
        title, ext = os.path.splitext(os.path.basename(pathAndFilename))
        os.rename(pathAndFilename,
                  os.path.join(dir, titlePattern % title + ext))

path = easygui.diropenbox()
print(path)
rename(path, r'*.png', r'p_%s')
