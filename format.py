__author__ = 'ffpku_000'
import os, re
os.chdir('C:/Users/ffpku_000/Documents/Research_Genome/Data/gameon/')

if __name__ == '__main__':

    with open('GameOnData.txt', 'w') as all_data:

        for task in range(1, 65):

            for old in os.listdir(os.getcwd()):
                if re.match('^Task_%r_Data' % task, old):
                    break
            with open(old) as old_file:
                data = old_file.readlines()

            with open(os.getcwd()+'\\reformat\\' + old, 'w') as new_file:
                for line in data:
                    temp = ' '.join(re.split("'+", line)[1:])
                    if not temp:
                        temp = '\n'
                    new_file.writelines(temp)
                    all_data.writelines(temp)

            print 'Task %r is reformatted now!' % task

    print 'All data reformatted now!'
