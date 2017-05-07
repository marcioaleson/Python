import unittest

HTML = '''\
<html>
    <head>
         <title>Unittest output</title>
    </head>
    <body>
         <table>
         {}
         </table>
    </body>
</html>'''

OK_TD = '<tr><td style="color: green;">{}</td></tr>'
ERR_TD = '<tr><td style="color: red;">{}</td></tr>'
