import requests
import pandas
import io
import csv


def download():
    # change group to CS for complete schedule
    p = {'Description': 'yes', 'Group': 'CS', 'Semester': '1188'}
    sess = requests.session()
    info = sess.post('https://rabi.phys.virginia.edu/mySIS/CS2/deliverData.php', p)
    data = pandas.read_csv(io.StringIO(info.text, "\n"), header=0)
    data.to_csv('lousdata.csv')

    print "data sync complete"


download()
