#EXTRACTING A LINK 
#All a web page is is a string. We have to find
#links and then extract them.
#Every link starts with <a href =

# Write Python code that initializes the variable
# start_link to be the value of the position
# where the first '<a href=' occurs in a page.

page =('<div id="top_bin"><div id="top_content" class="width960">'
'<div class="udacity float-left"><a href="http://udacity.com">')

start_link = page.find("<a href=", 0)

# Write Python code that assigns to the 
# variable url a string that is the value 
# of the first URL that appears in a link 
# tag in the string page.

# page = contents of a web page

start_url = page.find('http', start_link)
end_url = page.find('"', start_url)
url = page[start_url:end_url]
print url