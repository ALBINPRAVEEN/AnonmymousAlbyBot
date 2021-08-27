
#Function to send video
def sendMedia(update,context):
 try:
  update.message.reply_video(update.message.video.file_id)
 except Exception as e:
 	update.message.reply_text(e)
 
#Function to send file
def sendFile(update,context): 
 try:
  	update.message.reply_document(update.message.document.file_id)
 except Exception as e:
  	update.message.reply_text(e)
  	
#Function to send image
def sendPhoto(update,context):
 try:
   update.message.reply_photo(update.message.photo[-1].file_id)
 except Exception as e:
  	update.message.reply_text(e)
   
#Function to send text messages
def sendText(update,context):
 try:
   update.message.reply_text(update.message.text)
 except Exception as e:
  	update.message.reply_text(e)

#Function to send sticker
def sendSticker(update,context):
 try:
   update.message.reply_sticker(update.message.sticker.file_id)
 except Exception as e:
   update.message.reply_text(e)

#Function to send voice
def sendVoice(update,context):
 try:
   update.message.reply_voice(update.message.voice.file_id)
 except Exception as e:
  	update.message.reply_text(e)

#function to send audio
def sendAudio(update,context):
 try:
   update.message.reply_audio(update.message.audio.file_id)
 except Exception as e:
  	update.message.reply_text(e)
  
