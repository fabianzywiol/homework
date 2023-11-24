has_facebook = str(input("Do you have a facebook account? (True/False) "))
has_twitter = str(input("Do you have a twiiter account? (True/False) " ))
has_instagram = str(input("Do you have an instagram account? (True, False) "))

facebook = has_facebook.lower() == 'true'
twitter = has_twitter.lower() == 'true'
instagram = has_instagram.lower() == 'true'

can_be_influencer = (facebook and twitter) or (facebook and instagram) or (twitter and instagram)

if can_be_influencer:
    print("A person can be a good influencer!")
else:
    print("A person can't be a good influencer!")


