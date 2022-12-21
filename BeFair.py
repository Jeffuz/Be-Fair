import instaloader
import getpass

# Instance
L = instaloader.Instaloader()

# Prompts
input_prompts = {0:("Be Fair is a python script that can check who you follow, who follows you, and who you follow but don't follow back on Instagram."), 
                 1:("Please enter username: "), 
                 2:("Please enter password: "),
                 3:("\nWould you like to see a list of people you follow, people who follow you, or people you follow but do not follow you back?\
                    \nType 1 for following, 2 for followers, 3 for who you're following but who are not followers, 4 to quit: "),
                 4:("Incorrect option, please try again."),
                 5:("\nThank you, Goodbye!"),
                 6:("Incorrect credentials, Please try again.")}


# Login Info
print(input_prompts[0])
while True:
    try:
        username = input(input_prompts[1])
        password = getpass.getpass(input_prompts[2])
        L.login(username, password) 
    except: 
        print(input_prompts[6])
        continue
    break

profile = instaloader.Profile.from_username(L.context, username)

# profiles that are follow, followed, and intersections
followers = []
following = []
intersect = []

for x in profile.get_followers():
    followers.append(x.username)

for y in profile.get_followees():
    following.append(y.username)

for z in following:
    if z not in followers:
        intersect.append(z)

# user options
while True:
    options = input(input_prompts[3])
    if options == "1":
        print(f"The following usernames in the list are people you follow: {following}\n")
    elif options == "2":
        print(f"The following usernames in the list are people who follow you: {followers}\n")
    elif options == "3":
        print(f"The following usernames in the list are people you follow but do not follow you back: {intersect}\n")
    elif options == "4":
        print(input_prompts[5])
        exit()
    else:
        print(input_prompts[4])
        continue
    

