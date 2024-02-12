from imapclient import IMAPClient
import pyzmail
import re
import os

username = "tehran14001405@gmail.com"
password = "tbtf fyuw lnyk ruzb"
# username = "wwww23232sse@gmail.com"
# password = "vyfs lsjv nxwf nswi"

while True:
    try:
        client = IMAPClient('imap.gmail.com')
        client.login(username, password)
        client.select_folder('[Gmail]/Sent Mail')
        break
    except Exception as e:
        print(e)

list_dir = os.listdir()
for i in list_dir:
    try: os.remove(i + "\\link.txt")
    except: pass
    try: os.remove(i + "\\code.txt")
    except:pass

linkP = r'https://nobat.mex.co.ir/form/\?id=\w+'
print("Connected to Gmail")
CodeList = []
LinkList = []

while True:
    MESSAGES = client.search('ALL')
    if MESSAGES:
        msg_id = MESSAGES[-1]

        try:
            RAW_MSG = client.fetch([msg_id], ['BODY[]', 'FLAGS'])
            MSG = pyzmail.PyzMessage.factory(RAW_MSG[msg_id][b'BODY[]'])
            if MSG.text_part is not None:
                CTX = MSG.text_part.get_payload().decode(MSG.MSG.charset)
            elif MSG.html_part is not None:
                CTX = MSG.html_part.get_payload().decode(MSG.html_part.charset)
            else:
                print("This message does not have a text or HTML part.") 
            Sender = CTX[CTX.find("-") + 2: CTX.find("(")]
            if "8230" in Sender:
                pass
            else:
                continue
            BODY = CTX[CTX.find(":") + 2: CTX.rfind("(")]
            links = re.findall(linkP, BODY)
            if len(links) == 0:
                numbers = re.findall(r'\d+', BODY)[0]
                if numbers in CodeList:
                    continue
                print(numbers)
                CodeList.append(numbers)
                title = MSG.get_subject()
                filename = os.path.join(title[title.rfind(' ') + 1:], "code.txt")
                if not os.path.exists(filename):
                    with open(filename, "w") as f1:
                        f1.write(numbers)
            else:
                links = links[0]
                if links in LinkList:
                    continue
                print(links)
                LinkList.append(links)
                title = MSG.get_subject()
                filename = os.path.join(title[title.rfind(' ') + 1:], "link.txt")
                if not os.path.exists(filename):
                    with open(filename, "w") as f1:
                        f1.write(links)
        except Exception as e:
            print(e)