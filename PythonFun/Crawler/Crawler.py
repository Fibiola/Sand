#EXTRACTING A LINK
#All a web page is is a string. We have to find
#links and then extract them.
#Every link starts with <a href =

# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page ="""<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com"> <div> <a href="http://www.newlink.com">"""

start_link = page.find("<a href=", 0)

# Write Python code that assigns to the
# variable url a string that is the value
# of the first URL that appears in a link
# tag in the string page.

# page = contents of a web page

#start_url = page.find('"', start_link)
#end_url = page.find('"', start_url + 1)
#url = page[start_url + 1 :end_url]
#print url

#page = page[end_url:]
#start_link = page.find('<a href=')
#start_url = page.find('"', start_link)
#end_url = page.find('"', start_url + 1)
#url = page[start_url + 1:end_url]
#print url

# You can repeat this manually for all the links on the page. Or we use functions.

# PROCEDURE - AKA FUNCTION

# defined function - we change the name to a more generic name s as page.
def get_next_target(s):
	start_link = s.find('<a href=')
	start_quote = s.find('"', start_link)
	end_quote = s.find('"', start_quote + 1)
	url = s[start_quote + 1:end_quote]
	return url, end_quote

print get_next_target(page)
#side effect : something we see -> but we don't get it as an output.
#find is also a procedure!

# Modify the get_next_target procedure so that
# if there is a link it behaves as before, but
# if there is no link tag in the input string,
# it returns None, 0.

# Note that None is not a string and so should
# not be enclosed in quotes.

# Also note that your answer will appear in
# parentheses if you print it.

def get_next_target(page):
    start_link = page.find('<a href=')

    #Insert your code below here
    if start_link != 1:
        start_quote = page.find('"', start_link)
        end_quote = page.find('"', start_quote + 1)
        url = page[start_quote + 1:end_quote]
        return url, end_quote
    else:
        return None, 0


def print_all_links(pages):
    while True:
        url, endpos = get_next_target
        if url:
            print url
            page = page[endpos:]
        else:
            break

