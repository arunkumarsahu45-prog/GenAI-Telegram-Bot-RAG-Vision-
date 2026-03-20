from rag import retrieve, generate_answer
from vision import caption_image

async def ask(update, context):
    query = " ".join(context.args)

    docs = retrieve(query)
    context_text = "\n".join(docs)

    answer = generate_answer(context_text, query)

    await update.message.reply_text(answer)


async def image(update, context):
    photo = update.message.photo[-1]
    file = await photo.get_file()

    path = "img.jpg"
    await file.download_to_drive(path)

    caption, tags = caption_image(path)

    await update.message.reply_text(
        f"Caption: {caption}\nTags: {tags}"
    )


async def help_cmd(update, context):
    await update.message.reply_text(
        "/ask <question>\nSend image for caption\n/help"
    )