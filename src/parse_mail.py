#!/opt/lastlist/apps/python/venv3/bin/python
import uuid
import base64
from email.header import decode_header

def mail_parse(text):

    words = ['Message-ID', 'From', 'Subject', 'Date', 'subject','date', 'from']
    result ={'origTextLen':len(text) }
    bFirstLine = False
    body=[]

    for line in text.splitlines():
        if(bFirstLine):
            body.append(line)
            continue

        if(len(line.strip()) == 0 and bFirstLine==False):
            print(".....")
            bFirstLine=True
        else:
            line = line.strip()
            for word in words:
                if(line.startswith(word)):
                    result[word] = line[(len(word)+1):].strip()

            if(line.startswith("Content-Type")):
                result["Content-Type"] = line[13:-1].strip()

            if(line.startswith("boundary")):
                result["boundary"] = line.split('=')[1][1:-1]
    #result["Body"] = "\r\n".join(body)
    if 'Message-ID' not in result:
        result['Message-ID'] = uuid.uuid4().hex
    try:
        fix_subject(result)
    except Exception as subex:
        print(subex)

    return result

def fix_subject(result):
    if(result['Subject'].startswith('=?utf-8?B?')):
        try:
            result['Subject'] = base64.b64decode(result['Subject'][10:])
            result['Subject'] = result['Subject'].decode()
            result['SubjectType'] = 'utf-8/base64'
        except:
            print("er")

    if(result['Subject'].startswith('=?utf-8?Q?')):
        try:
            result['SubjectType'] = 'utf-8/quoted'
            result['Subject'] =decode_header(result['Subject'])[0][0].decode('utf-8')
        except:
            print("er2")

if __name__ == "__main__":

    read_data = None
    path = '/home/developer/newdev/mail.samp'
    with open(path) as f:
        read_data = f.read()

    parse_result = mail_parse(read_data)
    print( parse_result )



    odd = "=?utf-8?Q?Obamacare=27s=20birth=20control=20mandate=20gets=20rolled=20back=20&=20San=20Diego=20grapples=20with=20a=20deadly=20outbreak?="