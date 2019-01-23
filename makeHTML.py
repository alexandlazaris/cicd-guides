import os.path
# from pathlib import Path

openDOM = "<html><body>"
closeDOM = "</body></html>"
file_html_name = "index.html"

if os.path.exists(file_html_name) is False:
    print (file_html_name + " file does NOT exist, creating a new file")
    file_html = open(file_html_name, "a")
    file_html.close()
elif os.path.exists(file_html_name): 
    print (file_html_name + " file exists")
print ("continuing python script")

file_html = open('index.html', 'r+')
file_html.truncate(0) # need '0' when using r+
file_html.close()
file_html = open("index.html", 'w')
file_html.write(openDOM)

file_readME = open('README.md') #
line = file_readME.readline()
while line:
    if "#" in line: # is this line a title or link?
        title = line.split("#")[1] # hashtag is useful only for README in GitLab
        file_html.write('<h2 href=' + line + ' style="background-color: yellow">' + title + '</h2>')
    else: # otherwise it's a link
        file_html.write("<p>")  
        file_html.write('<a href=' + line + '"">' + line + '</a>')
        file_html.write("</p>")        
    line = file_readME.readline() # read the next line    
file_readME.close() # close the source 
file_html.write(closeDOM) 
file_html.close() # close the html
