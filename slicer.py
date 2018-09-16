#danicatuckova@gmail.com


#get user email

email = input("What is your email address?: ").strip()

#slice out user name

user = email[:email.index("@")]


#slice domain name

domain = email[email.index("@") + 1:]

#format message

string = "Your username is {} and your domain name is {}"
output = string.format(user, domain)

#display output message

print(output)
