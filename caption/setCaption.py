


#Function for adding caption
#to media such as audio,image,gifs and files
def setCaption(update,context):
  if update.message.reply_to_message is not None:
   fileCaption= update.message.text
   fileType=update.message.reply_to_message
   if fileType.document!=None:
     update.message.reply_document(
       update.message.reply_to_message.document.file_id,caption=fileCaption)
   elif fileType.video!=None:
     update.message.reply_video(
       update.message.reply_to_message.video.file_id,caption=fileCaption)
   elif fileType.audio!=None:
     update.message.reply_audio(
       update.message.reply_to_message.audio.file_id,caption=fileCaption)
   elif fileType.voice!=None:
     update.message.reply_voice(
       update.message.reply_to_message.voice.file_id,caption=fileCaption)
   elif fileType.photo!=None:
     update.message.reply_photo(update.message.reply_to_message.photo[-1].file_id,caption=fileCaption)
  else:
    update.message.reply_text(update.message.text)
