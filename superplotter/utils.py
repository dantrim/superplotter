import os
import commands
 
''' -------------------------------------------'''
'''  OS/Shell Methods                          '''
''' -------------------------------------------'''
def mkdir_if_needed(destdir, dbg) :
    '''
    Given a requested output directory, test if it already exists.
    If not, make it.
    '''
    if not os.path.isdir(destdir) :
        if dbg : print "Making directory %s" % str(destdir)
        cmd = "mkdir -p %s" % str(destir)
        print cmd
        commands.getoutput(cmd)
        
def mv_file_to_dir(filename, destdir, dbg) :
    '''
    Move a specified file to a given destination directory.
    First check if the directory exists. If not, make it.
    '''
    if not os.path.isdir(destdir) :
        if dbg : print "Making directory %s" % str(destdir)
        cmd = "mkdir -p %s" % str(destdir) 
        print cmd
        commands.getoutput(cmd)
    cmd = "mv %s %s" % (filename, destdir)
    print cmd
    commands.getoutput(cmd)
        
     
    
