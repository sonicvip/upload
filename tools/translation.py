class Translation(object):
    START_TEXT = """
π Forward any files to this bot,and bot will generate its directlink.
πDo not send multiple files at a time.
πIf you dont get directlink after 1 hour,forward that file again to the bot
πSubscribe our channel for bot updates @filestolink
πDirect links are only for personal use,do not share with others.we are not responsible for any content that you generates direct links.

    """
    HELP_USER = """
π Forward any files to this bot,and bot will generate its directlink.
π If you dont get directlink after 1 hour, forward that file again to the bot
π Direct links are only for personal use, do not share with others. We are not responsible for any content that you generates direct links.


    """
    ABS_TEXT = "Do not send multiple files at a time π«"
    DOWNLOAD_START = "π€ Your request is in the queue. Please be patient..."
    DOWNLOADING = "Downloading...π₯"
    SAVED_RECVD_DOC_FILE = "Document Downloaded Successfully...π₯"
    UPLOAD_START = "Started to upload...π€"
    AFTER_GET_DL_LINK = """
    <b>Direct Link generated π</b>
    
Name: {}
Size: {}
Expiry: {} days
Link : {}

<i>Join our channel</i> @keralasbots
    """
    ABUSIVE_USERS = "You got BANNED bro..."
