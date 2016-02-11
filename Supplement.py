__author__ = 'ffpku_000'
# As some pages cannot be reached by clicking on "Next" button on the page, those pages have to be searched again.

from GameOn.main import *
os.chdir('C:/Users/ffpku_000/Documents/Research_Genome/Data/gameon/')

if __name__ == '__main__':

    for task in range(1, 46):

        for old in os.listdir(os.getcwd()):
            if re.match('^Task_%r_Data' % task, old):
                break
        with open(old) as old_file:
            data = old_file.readlines()
        chr = re.split('_', old)[3]

        for i in range(0, len(data), 100):

            if data[i][0] == ' ':

                try:
                    start = int(data[i-1].split("''")[4]) + 1
                except IndexError:
                    start = re.split('_', old)[5]

                for login_i in login:

                    try:
                        driver = simple_load(*login_i, chr=chr, start=start)
                        time.sleep(5)
                        html = etree.HTML(driver.page_source)
                        tbody = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp"]/tbody/tr')
                        new_lines = [[td.text for td in tr] for tr in tbody]
                        for k in range(0, len(new_lines)):
                            data[i+k] = "'" + "''".join(new_lines[k]) + "'\n"
                        driver.close()
                        break

                    except:
                        pass

        with open(os.getcwd()+'\\final\\' + old, 'w') as new_file:
            new_file.writelines(data)

        print 'Task %r is complete now!' % task
