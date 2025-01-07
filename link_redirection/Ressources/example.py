def check_site(site):
    allowed_sites = ['google.com', 'facebook.com', 'twitter.com']
    if site in allowed_sites:
        return True
    return False