def create_single_text_message(message):
    if message == 'ありがとう':
        message = 'どういたしまして！'
    text_message = [
        {
            'type': 'text',
            'text': message
        }
    ]
    return text_message
