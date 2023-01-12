# CPU and RAM Web Monitor
This uses Python Bottle server as a backend and JavaScript as the frontend to serve CPU and RAM usage of a server over the internet using replit.

## Explaining the program
### Server.py
It contains code for providing the bottle sever all the code required for directing to the necessary files such index.html and front_end.js. It is necessary for providing the output and processing it from the input that is obtained from the frontend through javascript in the form of JSON blob

### App.py
It contains code for processing the data present by reading the CSV file and forming it into a format that plotly requires.

### frontend.js
It contains code for obtaining the data from the static HTML page and also proving an output in the HTML page by using the div id

## How is the Data obtained?
The data is obtained by creating a CSV file in the ubuntu server and continue running the code as a service in the server. The records are produced every five minutes and appended to the said file in the server.

## How is the file sent to reply?
The file is sent to replit by enabling an HTTP server of python3 in the server. Then on top of this, NGROK is used to make the HTTP server available for a short time. NGROK opens the HTTP port, allowing the code in the replit to request the CSV file to be downloaded.

## What can be done with the data?
* The data present in CPUUsage.csv allows data analysis on how much RAM and CPU utilization percentage is over time. It provides continuous measurements with an interval of 5 minutes.
The data present in memoryasservice.csv allows us to perform data analysis on how much each program has been using the RAM over a period of time.

* This helps keep track of the server and maintain a record easily without implementing Network Management Software and not spending any premium.

## What can be improved?
* The data from the server to replit can be sent more securely.
* The data can be updated more efficiently instead of sending the whole file itself.
