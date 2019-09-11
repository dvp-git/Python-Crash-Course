# Exerecise 8.13 User Profile


##Defining a function called sandwiches which accepts list of items a person wants
def build_profile(first, last, **user_info):
                """Build a dictionary containing everything we know about a user."""
                profile = {}
                profile['first_name'] = first
                profile['last_name'] = last
                for key, value in user_info.items():
                        profile[key] = value
                return profile



user_profile = build_profile('Darryl', 'Prabhu',location='mangalore',field='CS',language = 'python')
                
print(user_profile)
