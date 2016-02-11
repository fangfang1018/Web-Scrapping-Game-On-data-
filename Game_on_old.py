import time, os, selenium, re
from selenium import webdriver
from lxml import etree

os.chdir('C:/Users/ffpku_000/Documents/Research_Genome/Data/gameon/')


def scrap(email="fangf1018@gmail.com", passwd="fff11950",
          chr=None, start=None, end=None,
          data_file_name='Game_On_Data.txt', error_file_name='Game_On_Error_log.txt',
          error_summary_file_name='Error_Summary.txt'):
    url = 'http://gameon.dfci.harvard.edu/gameon'
    driver = webdriver.Chrome('C:/Program Files/chromedriver.exe')
    driver.get(url)
    assert 'Welcome to GAME-ON' in driver.title

    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="google_login_form"]/input[3]').click()

    time.sleep(1)
    driver.find_element_by_name("Email").send_keys(email)
    driver.find_element_by_name("signIn").submit()

    time.sleep(1)
    driver.find_element_by_name("Passwd").send_keys(passwd)
    driver.find_element_by_name("signIn").submit()

    time.sleep(5)
    try:
        driver.find_element_by_xpath('//*[@id="submit_approve_access"]').click()
        print 'Allow Access!'
    except Exception:
        pass

    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="termsofuse_checkbox"]').click()
    driver.find_element_by_name("btnAccept").click()

    if chr:
        driver.find_element_by_xpath('//*[@id="chromosome"]/option[text()="chr%s"]' % chr).click()
        driver.find_element_by_xpath('//*[@id="coordinateBox1"]').send_keys(str(start))
        driver.find_element_by_xpath('//*[@id="coordinateBox2"]').send_keys(str(end))
        driver.find_element_by_xpath('//*[@id="c_snprow"]/form/input[6]').click()

    # Scraping GWAS Table from Webpage

    j = -1
    data = []
    error = []
    data_file = open(data_file_name, 'w')
    error_file = open(error_file_name, 'w')
    error_summary_file = open(error_summary_file_name, 'a')

    total = 10000

    while j < total:

        t0 = time.time()
        t = 0
        while driver.find_element_by_xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_processing"]').is_displayed() \
                and t < 10:
            t = time.time() - t0

        html = etree.HTML(driver.page_source)
        tbody = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp"]/tbody/tr')
        ij = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_info"]')[0].text
        i = int(re.sub(',', '', re.split(' ', ij)[1]))
        j = int(re.sub(',', '', re.split(' ', ij)[3]))
        total = int(re.sub(',', '', re.split(' ', ij)[5]))
        new_lines = [[td.text for td in tr] for tr in tbody]

        if t < 10:

            # make sure the data table loaded from html have # of lines as stated
            try:
                assert (j - i + 1) == len(new_lines)
            except AssertionError:
                print 'Length different! %r new lines, but showing entries from %r to %r' % (len(new_lines), i, j)
                print new_lines

            # update and write to file
            for line in new_lines:
                data.append(line)
                for item in line:
                    data_file.write("%r" % item)
                data_file.write('\n')

        else:

            j += 100

            for line in new_lines:
                data.append(line)
                for item in range(0, 27):
                    data_file.write(" ")
                data_file.write('\n')

            error.append(str(j + 1) + '\n')
            # error_file.write(str(j+1)+'\n')
            coord_start = int(new_lines[-1][4]) + 1

            error_file.write(time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime()))
            error_file.write('%r %r %r %r %r\n' % (chr, start, end, (j + 1), coord_start))
            error_summary_file.write(time.strftime('%Y-%m-%d %H:%M:%S ', time.localtime()))
            error_summary_file.write('%r %r %r %r %r\n' % (chr, start, end, (j + 1), coord_start))

        # click "Next" to load data from next page
        driver.find_element_by_xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_next"]').click()

    data_file.close()
    error_file.close()
    error_summary_file.close()
    driver.close()
    return 1


def scrap_wapper(email="fangf1018@gmail.com", passwd="fff11950", task_num=None, task_path='task.txt',
                 data_file_name=None, error_file_name=None):
    task = (open(task_path, 'r')).readlines()
    task = [map(int, re.sub('\n', '', task_i).split()) for task_i in task]

    if not task_num:
        for task_i in task:
            # find the 1st task with status 0
            if not task_i[1]:
                task_num = task_i[0]
                break

    if not task_num:
        print 'No task specified. And all tasks have already been done!'
        return 2

    chr = task[task_num - 1][2]
    start = task[task_num - 1][3]
    end = task[task_num - 1][4]

    print 'Working on Task %r chr %r from coordinate %r to %r!' % (task_num, chr, start, end)

    if not data_file_name:
        data_file_name = 'Task_%r_Data_%s_cord_%r_to_%r.txt' % (task_num, chr, start, end)
    if not error_file_name:
        error_file_name = 'Task_%r_Error_%s_cord_%r_to_%r.txt' % (task_num, chr, start, end)

    status = scrap(email, passwd, chr, start, end, data_file_name, error_file_name)

    if status:
        task[task_num - 1][1] = 1
    else:
        task[task_num - 1][1] = 0

    task_file = open(task_path, 'w')
    for task_i in task:
        task_file.write(' '.join(map(str, task_i)) + '\n')

    if status:
        print 'Task %r Success!' % task_num
        return 1
    else:
        print 'Task %r Failed!' % task_num
        return 0


login0 = ("fangf1018@gmail.com", "fff11950")
login = [login0,
         ('game.on.data.1@gmail.com', 'gameondata'),
         ('game.on.data.2@gmail.com', 'gameondata'),
         ('game.on.data.3@gmail.com', 'gameondata'),
         ('game.on.data.4@gmail.com', 'gameondata'),
         ('game.on.data.5@gmail.com', 'gameondata'),
         ('game.on.data.6@gmail.com', 'gameondata'),
         ('game.on.data.7@gmail.com', 'gameondata'),
         ('game.on.data.8@gmail.com', 'gameondata'),
         ('game.on.data.9@gmail.com', 'gameondata'),
         ('game.on.data.10@gmail.com', 'gameondata'),
         ('game.on.data.11@gmail.com', 'gameondata'),
         ('game.on.data.12@gmail.com', 'gameondata'),
         ('game.on.data.13@gmail.com', 'gameondata'),
         ('game.on.data.14@gmail.com', 'gameondata'),
         ('game.on.data.15@gmail.com', 'gameondata'),
         ('game.on.data.16@gmail.com', 'gameondata'),
         ('game.on.data.17@gmail.com', 'gameondata'),
         ('game.on.data.18@gmail.com', 'gameondata'),
         ('game.on.data.19@gmail.com', 'gameondata'),
         ('game.on.data.20@gmail.com', 'gameondata'),
         ('game.on.data.21@gmail.com', 'gameondata'),
         ('game.on.data.22@gmail.com', 'gameondata'),
         ('game.on.data.23@gmail.com', 'gameondata'),
         ('game.on.data.24@gmail.com', 'gameondata'),
         ('game.on.data.25@gmail.com', 'gameondata'),
         ]

if __name__ == '__main__':

    # scrap_wapper(*login0, task_path='task_test.txt')
    # scrap_wapper(*login0, task_num=2, task_path='task_test.txt')

    # for login_i in login:
    #     print login_i
    #     try:
    #         scrap_wapper(*login_i)
    #     except:
    #         print '429 Error! '

        # scrap_wapper(*login0, task_path='task_sup.txt', task_num=1)
    scrap_wapper(*login[11], task_num=63, data_file_name='Task_63_Data.txt', error_file_name='Task_63_Error.txt')
