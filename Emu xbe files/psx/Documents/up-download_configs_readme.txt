The website that is used for uploading/downloading configuration data can be changed
by going to Netplay Options -> Enter XPort Website IP



Here is how a configuration is uploaded:

A POST is issued to the website with the following data:

---------BEGIN POST------------------
POST /upconfig.php HTTP/1.1
Host: xport.xbox-scene.com
Content-Type: application/x-www-form-urlencoded
Content-Length: %u

emu=%s&name=%s&datalen=%s&data=%s

------------END POST------------------

emu     : The platform name, all lower-case.  In the case of PCSXBox, this is psx.
          This value can always be obtained by navigating to your default screenshot
          directory and seeing what subdirectories are inside it.

name    : This is the filename that the user specified

datalen : this is the length of the binary data stream represented by "data"

data    : This is the binary configuration data.  Each byte has been url-encoded
          whether it needs it or not.  So this string will look like the following:
   
          %00%20%28%3E%DD%00 (and so on)


The server should then issue one of the following strings as a response:

^^^ : This means that configuration was successfully uploaded.

!!! : This means that the filename already exists.

@@@ : This means that some other error occurred.  


======================================================================================================


Here is how a listing of the configurations available for download is obtained:

The following "GET" is issued to the website:

---------BEGIN GET--------------
GET /configs.php?emu=%s HTTP/1.1
Host: xport.xbox-scene.com

--------END GET-------------

Where the variable after emu is the platform.  See "emu" above for more information 
about this.  (For PCSXBox, emu should be psx )

The server should respond with the following string:

%%%filename1|filename2|filename3|

This list is then displayed to the user and they can select which one to download.


======================================================================================================


Here is how a configuration is downloaded from the website:

The following "GET" is issued to the website:

-------------BEGIN GET---------------
GET /configs/%s/%s HTTP/1.1
Host: xport.xbox-scene.com

-------------END GET-------------------

Where the first %s should be replaced with the "emu" (described above)
(should be psx for PCSXBox) and the second %s should be the name of the
file to be downloaded.  This should be exactly the same as one of the
names that was retrieved from the server when the configuration list
was obtained.


Here is a specific example:

-------------BEGIN GET---------------
GET /configs/psx/alundra.cfg HTTP/1.1
Host: xport.xbox-scene.com

-------------END GET-------------------

This is a simple file get.  The GET points to a file.  The web server should respond in
the normal way for downloading a file.


Sample PHP files for configs.php and upconfig.php are included with this instruction
manual.
