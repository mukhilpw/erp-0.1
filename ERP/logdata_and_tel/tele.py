import requests
import os

bt = "7926394771:AAHUzy5-l0Uheu-ciPgLxsN095kGTvxRnPg"
cd = "-1002396692153"



def check_telegram_message_type(cd, message, file=None, file_type=None):
    if file and file_type:
        if file_type == "photo":
            send_telegram_image(cd, file)
            return "image"
        elif file_type == "document":
            send_telegram_document(cd, file)
            return "document"
        elif file_type == "audio":
            send_telegram_audio(cd, file)
            return "audio" 
        elif file_type == "video":
            send_telegram_video(cd, file)
            return "video"
        else:
            send_telegram_message(cd, message="Unsupported file type")
            return "unsupported"
    else:
        send_telegram_message(cd, message=message)
        return "text"

def send_telegram_image(cd, image):
    send_telegram_message(cd, message="Sending image")
    file_size = os.path.getsize(image)
    if file_size > 20000000:  # Telegram API limit for images is 20MB
        send_telegram_message(cd, message="Image size exceeds Telegram API limit")
        return "Error: Image size exceeds Telegram API limit"
    url = f"https://api.telegram.org/bot{bt}/sendPhoto?cd={cd}"
    response = requests.post(url, files={'photo': open(image, 'rb')})
    return response

def send_telegram_document(cd, document):
    send_telegram_message(cd, message="Sending document")
    file_size = os.path.getsize(document)
    if file_size > 200000000:  # Telegram API limit for documents is 200MB
        send_telegram_message(cd, message="Document size exceeds Telegram API limit")
        return "Error: Document size exceeds Telegram API limit"
    url = f"https://api.telegram.org/bot{bt}/sendDocument?cd={cd}"
    response = requests.post(url, files={'document': open(document, 'rb')})
    return response

def send_telegram_audio(cd, audio):
    send_telegram_message(cd, message="Sending audio")
    file_size = os.path.getsize(audio)
    if file_size > 20000000:  # Telegram API limit for audio is 20MB
        send_telegram_message(cd, message="Audio size exceeds Telegram API limit")
        return "Error: Audio size exceeds Telegram API limit"
    url = f"https://api.telegram.org/bot{bt}/sendAudio?cd={cd}"
    response = requests.post(url, files={'audio': open(audio, 'rb')})
    return response

def send_telegram_video(cd, video):
    send_telegram_message(cd, message="Sending video")
    file_size = os.path.getsize(video)
    if file_size > 200000000:  # Telegram API limit for videos is 200MB
        send_telegram_message(cd, message="Video size exceeds Telegram API limit")
        return "Error: Video size exceeds Telegram API limit"
    url = f"https://api.telegram.org/bot{bt}/sendVideo?cd={cd}"
    response = requests.post(url, files={'video': open(video, 'rb')})
    return response

def send_telegram_message(cd, message=None, file=None, file_type=None):
    message_type = check_telegram_message_type(cd, message, file, file_type)
    if message_type == "image":
        return send_telegram_image(cd, file)
    elif message_type == "document":
        return send_telegram_document(cd, file)
    elif message_type == "audio":
        return send_telegram_audio(cd, file)
    elif message_type == "video":
        return send_telegram_video(cd, file)
    elif message_type == "text":
        try:
            if message:
                url = f"https://api.telegram.org/bot{bt}/sendMessage?cd={cd}&text={message}"
                response = requests.get(url)
                return response
        except Exception as e:
            return f"Error sending message: {str(e)}"
    else:
        return "Error: Unsupported message type"
































def send_telegram_message(cd, message=None, file=None, file_type=None):
    if not file and not message:
        return "No message or file provided"
    if file:
        file_size = os.path.getsize(file)
        print("file_size",file_size)
        if file_size > 10000000:
            send_large_file(cd, file, file_type)
    else:
        try:
            if message:
                url = f"https://api.telegram.org/bot{bt}/sendMessage?cd={cd}&text={message}"
                response = requests.get(url)
                return response
        except Exception as e:
            return f"Error sending message: {str(e)}"
    return None






def send_telegram_message_only(cd, message):
    try:
        url = f"https://api.telegram.org/bot{bt}/sendMessage?cd={cd}&text={message}"
        response = requests.get(url)
        return response
    except Exception as e:
        return f"Error sending message: {str(e)}"
    


def send_telegram_message(cd, message=None, file=None, file_type=None):
    if not file and not message:
        return "No message or file provided"
    if file:
        file_size = os.path.getsize(file)
        print("file_size",file_size)
        if file_size > 10000000:
            send_large_file(cd, file, file_type)
    else:
        try:
            if message:
                url = f"https://api.telegram.org/bot{bt}/sendMessage?cd={cd}&text={message}"
                response = requests.get(url)
                return response
        except Exception as e:
            return f"Error sending message: {str(e)}"
    return None


def upload_file_to_telegram(file_path, cd, message=None):
    send_telegram_message(cd, message=message, file=file_path, file_type="document")

def send_model_data_to_telegram(model_data, cd):
    message = str(model_data)
    send_telegram_message(cd, message=message)

# Example usage:
# upload_file_to_telegram("path/to/file.pdf", cd)
# send_model_data_to_telegram(Vehicle.objects.get(id=1), cd)




# def send_telegram_message(cd, message=None, file=None, file_type=None):
    
#     if file:
#         file_size = os.path.getsize(file)
#         print("file_size",file_size)
#         if file_size > 10000000:
#             send_large_file(cd, file, file_type)
#     else:
#         try:
#             if message:
#                 url = f"https://api.telegram.org/bot{bt}/sendMessage?cd={cd}&text={message}"
#                 response = requests.get(url)
#                 return response
            
#             if file:
#                 if file_type in ["image", "audio", "video", "voice", "document"]:
#                     url = f"https://api.telegram.org/bot{bt}/send{file_type.capitalize()}?cd={cd}"
#                     try:
#                         with open(file, 'rb') as f:
#                             response = requests.post(url, files={"file": f})
#                             return response
#                     except FileNotFoundError:
#                         return "File not found"
#                     except Exception as e:
#                         return f"Error sending file: {str(e)}"
#                 else:
#                     return "Invalid file type"
#         except Exception as e:
#             return f"Error sending message: {str(e)}"
#     return None


# Example usage:
# send_telegram_message("YOUR_cd", "Hello, world!")
# send_telegram_message("YOUR_cd", file="path/to/image.jpg", file_type="image")

# To avoid file size error, you can use the following approach
def send_large_file(cd, file, file_type):
    url = f"https://api.telegram.org/bot{bt}/send{file_type.capitalize()}?cd={cd}"
    chunk_size = 1024 * 1024  # 1MB chunks
    try:
        with open(file, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                response = requests.post(url, files={"file": chunk})
                if response.status_code != 200:
                    return "Failed to send large file. Please check file size."
                    break
    except FileNotFoundError:
        return "File not found"
    except Exception as e:
        return f"Error sending large file: {str(e)}"
    return

# Example usage:
# send_large_file("YOUR_cd", "path/to/large/file.mp4", "video")

