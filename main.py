import time, os, re
from selenium import webdriver
from lxml import etree

os.chdir('C:/Users/ffpku_000/Documents/Research_Genome/Data/gameon/')
url = 'http://gameon.dfci.harvard.edu/gameon'

login_s = [('game.on.data.1@gmail.com', 'gameondata'),
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

login = login_s[6:]

'''
class GameOnDriver:

    def __init__(self, email=None, passwd=None, chr=None, start=None, end=None):
        self.email = email
        self.passwd = passwd
        self.chr = chr
        self.start = start
        self.end = end

    def search(self):

        driver = webdriver.Chrome('C:/Program Files/chromedriver.exe')
        driver.get(url)
        assert 'Welcome to GAME-ON' in driver.title

        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="google_login_form"]/input[3]').click()

        time.sleep(1)
        driver.find_element_by_name("Email").send_keys(self.email)
        driver.find_element_by_name("signIn").submit()

        time.sleep(1)
        driver.find_element_by_name("Passwd").send_keys(self.passwd)
        driver.find_element_by_name("signIn").submit()

        time.sleep(3)
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
            driver.find_element_by_xpath('//*[@id="coordinateBox1"]').send_keys(str(self.start))
            driver.find_element_by_xpath('//*[@id="coordinateBox2"]').send_keys(str(self.end))
            driver.find_element_by_xpath('//*[@id="c_snprow"]/form/input[6]').click()

        return driver


    def next(self):
'''


def load_page(email, passwd, chr=None, start=None, end=None):

    try:

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

        time.sleep(1)
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

        t0 = time.time()
        t = 0
        while driver.find_element_by_xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_processing"]').is_displayed() \
                and t < 10:
            t = time.time() - t0

        if t >= 10:
            print 'Loading Failed!'
            driver.close()
            return None

        assert 'GAME-ON' in driver.title
        return driver

    except:
        driver.close()
        return None


def simple_load(email=None, passwd=None, chr=None, start=None, end=None):

    if (email is None) or (passwd is None):
        for login_i in login:
            driver = load_page(*login_i, chr=chr, start=start, end=end)
            if driver is not None:
                print login_i
                return driver

    else:
        driver = load_page(email, passwd, chr, start, end)

    return driver


def scrap(email=None, passwd=None, chr=None, start=None, end=None, data_file_name='Game_On_Data.txt'):

    driver = simple_load(email, passwd, chr, start, end)

    # Scraping GWAS Table from Webpage
    j = -1
    total = 0
    data = []
    data_file = open(data_file_name, 'w')

    while j < total:

        t0 = time.time()
        t = 0
        while driver.find_element_by_xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_processing"]').is_displayed() \
                and t < 10:
            t = time.time() - t0

        if t >= 10:

            print j, 'new cycle'
            if len(data) > 0:
                start = int(data[-1][4]) + 1
                print data[-1]

            driver.close()
            print email, passwd, chr, start, end
            driver = simple_load(email, passwd, chr, start, end)

        html = etree.HTML(driver.page_source)
        tbody = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp"]/tbody/tr')
        ij = html.xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_info"]')[0].text
        i = int(re.sub(',', '', re.split(' ', ij)[1]))
        j = int(re.sub(',', '', re.split(' ', ij)[3]))
        total = int(re.sub(',', '', re.split(' ', ij)[5]))
        new_lines = [[td.text for td in tr] for tr in tbody]

        # make sure the data table loaded from html have # of lines as stated
        assert (j - i + 1) == len(new_lines)

        # update and write to file
        for line in new_lines:
            data.append(line)
            for item in line:
                data_file.write("%s " % item)
            data_file.write('\n')

        # click "Next" to load data from next page
        driver.find_element_by_xpath('//*[@id="l_edu_dfci_cccb_gameon_domain_Snp_next"]').click()

    data_file.close()
    driver.close()
    return data


def scrap_wapper(email=None, passwd=None, task_num=None, task_path='task.txt', data_file_name=None):

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

    status = scrap(email, passwd, chr, start, end, data_file_name)

    if status:
        task[task_num - 1][1] = 1
    else:
        task[task_num - 1][1] = 0

    task_file = open(task_path, 'w')
    for task_i in task:
        task_file.write(' '.join(map(str, task_i)) + '\n')

    if status:
        print 'Task %r Success!' % task_num
    else:
        print 'Task %r Failed!' % task_num

    return status


if __name__ == '__main__':

    pass

