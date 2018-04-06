import requests
import pandas
import io
import csv


def download():
    # change group to CS for complete schedule
    p = {'Description': 'yes', 'Group': 'CompSci', 'Semester': '1188'}
    sess = requests.session()
    info = sess.post('https://rabi.phys.virginia.edu/mySIS/CS2/deliverData.php', p)
    data = pandas.read_csv(io.StringIO(info.text, "\n"), header=0, encoding='utf-8')
    # file = open("data.txt", "w")
    # file.write(info.text.encode('utf-8'))
    # print info.text

    print "finished"


download()
