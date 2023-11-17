import time 
from plyer import notification 

if __name__ == "__main__":
    notification.notify(
        title = "Dictionary - Today's Word",
        message = "Clever - quick to understand, learn, and devise or apply ideas; intelligent.",
        
        timeout = 8
    )