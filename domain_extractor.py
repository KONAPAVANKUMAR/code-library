
def domain_name_1(url):

    full_domain_name = url.split('//')[-1] 
    actual_domain = full_domain_name.split('.')  
    if (len(actual_domain) > 2):
        return actual_domain[1]    
    return actual_domain[0]

def domain_name_2(url):
    return url.split("//")[-1].split("www.")[-1].split(".")[0]

