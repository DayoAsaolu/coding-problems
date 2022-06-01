def uniqueEmail(emails):

    uniqueEmail = set()

    for i in emails:
        plus = ""
        dot = ""
        x = i.split("@")

        if "+" in i:
            
            plueRule = x[0].split("+", 1)
            dotRule = plueRule[0].replace(".", "")
            unique = dotRule + "@" + x[1]
            uniqueEmail.add(unique)

        elif "." in x[0]:
            dotRule = x[0].replace(".", "")
            unique = dotRule + "@" + x[1]
            uniqueEmail.add(unique)
        
        
    return len(uniqueEmail)


def main():
    emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

    print(uniqueEmail(emails))
    return 0


main()