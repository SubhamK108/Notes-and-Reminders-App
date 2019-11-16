import os


def Create_Notes(note, filename):
    os.system('touch Notes/{0}.txt'.format(filename))
    file = open(r"Notes/{0}.txt".format(filename), "a")
    file.writelines(note)
    file.close()

def View_Notes(filename):
    try:
        file = open(r"Notes/{0}.txt".format(filename), "r")
    except:
        print('No notes are found on this date !')
        exit()
    notes = file.read()
    file.close()
    return notes

def Delete_Note(filename):
    try:
        file = open(r"Notes/{0}.txt".format(filename), "r")
    except:
        print('No notes are found on this date !')
        exit()
    file.close()
    os.system('rm -r Notes/{0}.txt'.format(filename))
