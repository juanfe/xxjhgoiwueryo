'''
Created on Feb 21, 2012

@author: Camilo
'''

#from google.appengine.ext import db, webapp
#from google.appengine.api import users
from user import getUser
#from model.loan import Loan, getLoan
from bid import Bid
from loan import getLoan
import datetime
from user import PageAllowed


class BidsInstance():
    def  UpdateDemoData(self):
        self.get()

    
    def get(self):
        #"3:00:00 PM";1104134;"1104134@test.com";"General";" $15,000,000.00
        #";"10%";;;;;"Noncompetitive";;"Auto";"12/15/11 12:53 PM"
        Bid( key_name="3:00:00 PM 1104134",
                bidtype = 'General',
                user = getUser('1104134@test.com'),
                aggregated = 15000000.00,
                status = 'Active',
                participation = 0.10,
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("3:00:00 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Auto",
                orderAt = datetime.datetime.strptime("12/15/11 12:53 PM", "%m/%d/%y %I:%M %p")
                ).put()

        #"3:00:00 PM";1104143;"1104143@test.com";"Specified";;;"20%";"MO";;"ABC
        #Mortgage";"Noncompetitive";;"Auto";"12/20/11 8:43 AM"
        Bid( key_name="3:00:00 PM 1104143",
                bidtype = 'Specified',
                user = getUser('1104143@test.com'),
                status = 'Active',
                participation = 0.20,
                lorm = "MO",
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("3:00:00 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Auto",
                mo = getUser('ABCD@test.com'),
                orderAt = datetime.datetime.strptime("12/20/11 8:43 AM", "%m/%d/%y %I:%M %p")
                ).put()

        #"3:00:00 PM";1104154;"1104154@test.com";"General";" $20,000,000.00
        #";"20%";;;;;"Competitive";"3.000%";"Auto";"1/5/12 9:16 AM"
        Bid( key_name="3:00:00 PM 1104154",
                bidtype = 'General',
                user = getUser('1104154@test.com'),
                aggregated = 20000000.00,
                status = 'Active',
                participation = 0.20,
                ordertype = "Competitive",
                bidrate = 0.03,
                createdAt = datetime.datetime.strptime("3:00:00 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Auto",
                orderAt = datetime.datetime.strptime("1/5/12 9:16 AM", "%m/%d/%y %I:%M %p")
                ).put()

        #"3:00:00
        #PM";1104152;"1104152@test.com";"Specified";;;"20%";"MO";;"Prime
        #Lending";"Competitive";"3.000%";"Auto";"1/5/12 9:15 AM"
        Bid( key_name="3:00:00 PM 1104152",
                bidtype = 'Specified',
                user = getUser('1104152@test.com'),
                status = 'Active',
                participation = 0.20,
                lorm = "MO",
                ordertype = "Competitive",
                bidrate = 0.03,
                createdAt = datetime.datetime.strptime("3:00:00 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                mo = getUser('BCDE@test.com'),
                ordertiming = "Auto",
                orderAt = datetime.datetime.strptime("1/5/12 9:15 AM", "%m/%d/%y %I:%M %p")
                ).put()

        #"5:06:12
        #PM";1104136;"1104136@test.com";"Specified";;;"20%";"Loan";4;;"Competitive";"6.000%";"Day
        #Trade";
        Bid( key_name="5:06:12 PM 1104136",
                bidtype = 'Specified',
                user = getUser('1104136@test.com'),
                status = 'Active',
                participation = 0.20,
                lorm = "Loan",
                loan = getLoan("201149669"),
                ordertype = "Competitive",
                bidrate = 0.06,
                createdAt = datetime.datetime.strptime("5:06:12 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"6:32:36 PM";1104138;"1104138@test.com";"General";" $1,000,000.00
        #";"50%";;;;;"Competitive";"2.125%";"Day Trade";
        Bid( key_name="6:32:36 PM 1104138",
                bidtype = 'General',
                user = getUser('1104138@test.com'),
                aggregated = 1000000.00,
                status = 'Active',
                participation = 0.50,
                ordertype = "Competitive",
                bidrate = 0.02125,
                createdAt = datetime.datetime.strptime("6:32:36 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"7:15:48 PM";1104139;"1104139@test.com";"General";" $500,000.00
        #";"30%";;;;;"Competitive";"2.250%";"Day Trade";
        Bid( key_name="7:15:48 PM  1104139",
                bidtype = 'General',
                user = getUser('1104139@test.com'),
                aggregated = 500000.00,
                status = 'Active',
                participation = 0.30,
                ordertype = "Competitive",
                bidrate = 0.02250,
                createdAt = datetime.datetime.strptime("7:15:48 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"7:59:00
        #PM";1104140;"1104140@test.com";"Specified";;;"20%";"Loan";5;;"Competitive";"2.500%";"Day
        #Trade";
        Bid( key_name="7:59:00 PM 1104140",
                bidtype = 'Specified',
                user = getUser('1104140@test.com'),
                status = 'Active',
                participation = 0.20,
                lorm = "Loan",
                loan = getLoan("201148440"),
                ordertype = "Competitive",
                bidrate = 0.0250,
                createdAt = datetime.datetime.strptime("7:59:00 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"8:42:12 PM";1104141;"1104141@test.com";"General";" $500,000.00
        #";"20%";;;;;"Competitive";"2.500%";"Day Trade";
        Bid( key_name="8:42:12 PM 1104141",
                bidtype = 'General',
                user = getUser('1104141@test.com'),
                aggregated = 500000.00,
                status = 'Active',
                participation = 0.20,
                ordertype = "Competitive",
                bidrate = 0.0250,
                createdAt = datetime.datetime.strptime("8:42:12 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"9:39:48
        #PM";1104159;"1104159@test.com";"Specified";;;"20%";"Loan";1;;"Noncompetitive";;"Day
        #Trade";
        Bid( key_name="9:39:48 PM 1104159",
                bidtype = 'Specified',
                user = getUser('1104159@test.com'),
                status = 'Active',
                participation = 0.0200,
                lorm = "Loan",
                loan = getLoan("201148329"),
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("9:39:48 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"11:06:12
        #PM";1104161;"1104161@test.com";"Specified";;;"20%";"Loan";4;;"Noncompetitive";;"Day
        #Trade";
        Bid( key_name="11:06:12 PM 1104161",
                bidtype = 'Specified',
                user = getUser('1104161@test.com'),
                status = 'Active',
                participation = 0.20,
                lorm = "Loan",
                loan = getLoan("201149669"),
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("11:06:12 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"11:35:00
        #PM";1104145;"1104145@test.com";"Specified";;;"10%";"Loan";1;;"Competitive";"1.500%";"Day
        #Trade";
        Bid( key_name="11:35:00 PM 1104145",
                bidtype = 'Specified',
                user = getUser('1104145@test.com'),
                status = 'Active',
                participation = 0.10,
                lorm = "Loan",
                loan = getLoan("201148329"),
                ordertype = "Competitive",
                bidrate = 0.0150,
                createdAt = datetime.datetime.strptime("11:35:00 PM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"2:23:00
        #AM";1104133;"1104133@test.com";"Specified";;;"20%";"Loan";4;;"Competitive";"4.000%";"Day
        #Trade";
        Bid( key_name="2:23:00 AM 1104133",
                bidtype = 'Specified',
                user = getUser('1104133@test.com'),
                status = 'Active',
                participation = 0.200,
                lorm = "Loan",
                loan = getLoan("201149669"),
                ordertype = "Competitive",
                bidrate = 0.040,
                createdAt = datetime.datetime.strptime("2:23:00 AM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"2:27:48
        #AM";1104149;"1104149@test.com";"Specified";;;"20%";"Loan";5;;"Noncompetitive";;"Day
        #Trade";
        Bid( key_name="2:27:48 AM 1104149",
                bidtype = 'Specified',
                user = getUser('1104149@test.com'),
                status = 'Active',
                participation = 0.200,
                lorm = "Loan",
                loan = getLoan("201148440"),
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("2:27:48 AM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"3:54:12
        #AM";1104151;"1104151@test.com";"Specified";;;"20%";"Loan";1;;"Noncompetitive";;"Day
        #Trade";
        Bid( key_name="3:54:12 AM 1104151",
                bidtype = 'Specified',
                user = getUser('1104151@test.com'),
                status = 'Active',
                participation = 0.200,
                lorm = "Loan",
                loan = getLoan("201148329"),
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("3:54:12 AM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"4:37:24 AM";1104131;"1104131@test.com";"General";" $1,000,000.00
        #";"50%";;;;;"Noncompetitive";;"Day Trade";
        Bid( key_name="4:37:24 AM 1104131",
                bidtype = 'General',
                user = getUser('1104131@test.com'),
                aggregated = 1000000.00,
                status = 'Active',
                participation = 0.500,
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("4:37:24 AM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"6:47:00 AM";1104155;"1104155@test.com";"Specified";;;"20%";"MO";;"Best
        #Loans Inc";"Competitive";"2.125%";"Day Trade";
        Bid( key_name="6:47:00 AM 1104155",
                bidtype = 'Specified',
                user = getUser('1104155@test.com'),
                status = 'Active',
                participation = 0.20,
                lorm = "MO",
                ordertype = "Competitive",
                bidrate = 0.02125,
                createdAt = datetime.datetime.strptime("6:47:00 AM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                mo = getUser('EFGH@test.com'),
                ordertiming = "Day Trade"
                ).put()

        #"7:30:12
        #AM";1104156;"1104156@test.com";"Specified";;;"20%";"Loan";2;;"Noncompetitive";;"Day
        #Trade";
        Bid( key_name="7:30:12 AM 1104156",
                bidtype = 'Specified',
                user = getUser('1104156@test.com'),
                status = 'Active',
                participation = 0.200,
                lorm = "Loan",
                loan = getLoan("201148009"),
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("7:30:12 AM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"8:13:24 AM";1104157;"1104157@test.com";"General";" $1,000,000.00
        #";"30%";;;;;"Noncompetitive";;"Day Trade";
        Bid( key_name="8:13:24 AM 1104157",
                bidtype = 'General',
                user = getUser('1104157@test.com'),
                aggregated = 1000000.00,
                status = 'Active',
                participation = 0.30,
                ordertype = "Noncompetitive",
                createdAt = datetime.datetime.strptime("8:13:24 AM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()

        #"8:56:36
        #AM";1104158;"1104158@test.com";"Specified";;;"20%";"Loan";1;;"Competitive";"2.250%";"Day
        #Trade";
        Bid( key_name="8:56:36 AM 1104158",
                bidtype = 'Specified',
                user = getUser('1104158@test.com'),
                status = 'Active',
                participation = 0.20,
                lorm = "Loan",
                loan = getLoan("201148329"),
                ordertype = "Competitive",
                bidrate = 0.02250,
                createdAt = datetime.datetime.strptime("8:56:36 AM", "%I:%M:%S %p"),
                expiresAt = datetime.datetime.strptime("12/15/13 12:53 PM", "%m/%d/%y %I:%M %p"),
                ordertiming = "Day Trade"
                ).put()
