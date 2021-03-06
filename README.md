Exchange Rate Alert
---

Creates desktop alerts when the Transferwise exchange rates hit a target rate. Checks conversion rate every time the polling interval has passed.

![Notification](./img/era_notification.jpg)

Currently running on Windows and Linux, PIP version 20.0.1

---

#### Before Using

Before the module can be used the user has to create a Transferwise API token. The detailed instructions can be found here - https://api-docs.transferwise.com/#payouts-guide-api-access  

The program will try and find the access token in the following manner
 
 1. System Variable named TCR - create a system variable named TCR
 
 2. Configuration file - located at `%HOMEDRIVE%%HOMEPATH%/.tcr` on windows or `~/.tcr` on linux

Add the token information in the file

    [default]
    token=aaaaaaaaa-bbbb-cccc-dddd-eeeeeeeeee
                      
---

#### Installation 

Install package from pip 
- `pip install exchange-rate-alert`

---

#### Usage

**1. From Command Prompt** 

- `era --source SEK --target INR --alert-rate 8.5 --poll-interval=30`

    ![CMD](./img/era_cli_option.JPG)
    
- `era` and respond to prompts

    ![CMD_PROMPTS](./img/era_cli_with_prompts.JPG)
    
   
**2. As a python module** 

Import into python script
- `from ratealert import ConversionAlert`
    
Call the constructor, wait for alert, profit!
- `ConversionAlert(source, target, alert_rate, poll_interval)`

**Example**

    from ratealert import ConversionAlert
    ConversionAlert('SEK', 'INR', 8.5, 60)

This will create a notification when the Transferwise exchange rate crosses the alert rate. 

![Notification](./img/era_notification.jpg)

The rates will be checked every 60 seconds if the polling interval option is not provided.

Exit the script by Ctrl+C

---

#### Change notes

0.8 - Polling interval as an option, minor fix for Linux

0.7 - support for Linux, installs packages based on OS

0.6 - Command line execution, input prompts

0.3 - Alert on a target conversion rate
 
0.1 - Alert at specified intervals


---

#### Next steps

- Quotation request and transfer lock on target conversion rate
- OAuth login for Transferwise
- Support for other clients (Remitly?) 

