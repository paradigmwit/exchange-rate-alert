# Exchange Rate Alert
---

Creates desktop alerts for Transferwise rate alerts at specified intervals in seconds.

---

#### Before Using
Before the module can be used the user has to create a Transferwise API token. The detailed instructions can be found here - https://api-docs.transferwise.com/#payouts-guide-api-access  

The program will try and find the access token in the following manner
 
 1. System Variable named TCR - create a system variable named TCR
 
 2. Configuration file - located at `%HOMEDRIVE%%HOMEPATH%/.tcr` on windows or `~/.tcr` on linux
                      
---

#### Usage 

`from ratealert.conversionalert import ConversionAlert
ConversionAlert(source, target, interval)`

#### Example

`from ratealert.conversionalert import ConversionAlert
ConversionAlert('SEK', 'INR', 300)`

This will create exchange rate alerts every 5 minutes. 

---

#### Next steps

- Alert on a target conversion rate
- Quotation request on target conversion rate
