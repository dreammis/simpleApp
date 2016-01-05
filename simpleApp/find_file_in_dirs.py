#01
def useGlob():
    '''
    :return:
    '''
    import os
    import glob
    #set the workDir
    os.chdir('/')
    for files in glob.glob('*.txt'):
        print files



def useWalk():
    import os
    #p:dirpath,n:dirnames,f:filenames
    for p,n,f in os.walk('C:/Users/admin/Desktop/Space/2.x-4.x'):
        for files in f:
            if files.endswith('.txt'):
                print os.path.join(p,files)

def useLd():
    import os
    for files in os.listdir('C:/Users/admin/Desktop/Space/2.x-4.x'):
        if files.endswith('.txt'):
            print files


keys = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')

dict = {}
dict.fromkeys(keys,values)