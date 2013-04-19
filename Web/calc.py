from datetime import datetime
from LiqSpot import LiqEngine
from model import loansModel
from google.appengine.ext import db


def CallEngine():
    eng = LiqEngine()
    #TODO add LSSpread and PriorDayRateUsed from config
    eng.setParameters(LSSpread = 1, PriorDayRateUsed = 3.5)

    mortop = db.GqlQuery("SELECT * "
            "FROM User Where group = 'MO'")
    mo = []
    for m in mortop:
        mo.append(m.key().name())
    eng.setMortgageOriginator(mo)

    #TODO only set loans who are involved in the calc
    loans = db.GqlQuery("SELECT * "
            "FROM loansModel ")
    s = []
    for l in loans:
        s.append({'loanId': l.key().name(),
                'mortgageOriginator': l.customer_account_key,
                 'loanAmount': l.curr_upb})
    eng.setLoans(s)

    users = db.GqlQuery("SELECT * "
            "FROM User Where group = 'Broker'")
    usr = []
    for u in users:
        usr.append({'userId': u.key().name(),
                'fundsAvailable': u.fundsAvailable})
    eng.setUsers(usr)

    bids = db.GqlQuery("SELECT * "
            "FROM Bid")
    s = []
    for b in bids:
        d = {'date': b.createdAt, 'bidId': b.key().name()}
        d['userId'] = b.user.key().name()
        d['bidType'] = b.bidtype
        if b.bidtype == 'Specified':
            d['assetSubset'] = b.lorm
        d['Participation'] = b.participation
        d['Aggregate'] = b.aggregated
        if b.lorm == "Loan":
            d['loanId'] = b.loan.key().name()
        elif b.lorm == "MO":
            d['mortgageOriginator'] = b.mo.key().name()
        d['orderTiming'] = b.ordertiming
        d['orderType'] = b.ordertype
        if b.ordertype == 'Competitive':
            d['bidRate'] = b.bidrate
        #if b.ordertiming == 'Auto':
        #    d[''] = b.orderAt
        s.append(d)

    eng.setBids(s)
    return eng.Calc()


def calc():
    try:
        context = CallEngine()

        Context = {}
        Context['loans'] = []
        for c in context['loans'].iteritems():
            Context['loans'].append(c[0])
        Context['bids'] = []
        for b in context['bids'].iteritems():
            c = [{'bid': b[0]}]
            for l in Context['loans']:
                if l in b[1]['allocatedAmounts']:
                    c.append(({"key": l, "val": '%.2f' %
                            b[1]['allocatedAmounts'][l]}))
                else:
                    c.append(({"key": l, "val": 0}))
            Context['bids'].append(c)
        return Context
    except:
        return None
