# Globals
from bs4 import BeautifulSoup
import re
import csv
import sys
renderClass = {'_ngcontent-server-side-render-c335': ''}


def main():
    if(len(sys.argv) < 2):
        return ""
    scapeFile = sys.argv[1]
    writeFile = sys.argv[2]
    with open(scapeFile) as fp:
        soup = BeautifulSoup(fp, 'html.parser')
    # soup = BeautifulSoup("<html>a web page</html>", 'html.parser')

    soup = soup.find('table', id='playerTransactionTable').tbody
    rows = soup.find_all('tr', renderClass)

    lst = []
    for row in rows:
        event1 = findTransaction(row, 3)
        event2 = findTransaction(row, 4)
        obj = {
            "date": findDate(row),
            "transaction": findTransaction(row, 0),
            "selection":  findTransaction(row, 2),
            "event": event1 if (event2 == None) else "%s | %s" % (event2, event1),
            "amount": findTransactionAmount(row),
            # "Value4": "1"
        }
        lst.append(obj)

    formattedList = formatLst(lst)
    writeToCSV(formattedList, writeFile)
    return "Sucessfully scraped %s and exported to %s" % (scapeFile, writeFile)


def findDate(row):
    dateTime = row.find(
        'td', {"class": 'date-field bx-transaction-date'}).find_all('span', renderClass)
    return '%s %s' % (dateTime[0].text, dateTime[1].text)


def findTransaction(row, n):
    tx = row.find('td', {
        "class": "transaction-field bx-transaction-description transaction-hidden-xs highlighted-tx-title"}).find_all('span', renderClass)
    try:
        s = tx[n].text.strip()
        s = s.replace('\n', '')
        s = re.sub('\s+', ' ', s)
        return s
    except:
        return None


def findTransactionAmount(row):
    amt = row.find(
        'td', {'class': 'amount-balance-field bx-transaction-amount'}).find_all('span')
    # print(amt[0]['data-amount'])
    return amt[0]['data-amount']


def formatLst(lst):
    headers = ['Date', 'Transaction', 'Selection', 'Event', 'Amount']
    newLst = [headers]
    for li in lst:
        newLst.append([li['date'], li['transaction'],
                      li['selection'], li['event'], li['amount']])
    return newLst


def writeToCSV(myList, filePath):
    # myFile = open(filePath, 'w)
    with open(filePath, 'w') as myfile:
        wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
        wr.writerows(myList)


if __name__ == '__main__':
    result = main()
    print(result)
