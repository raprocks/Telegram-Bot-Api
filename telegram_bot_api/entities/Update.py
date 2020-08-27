

class Update:
    def __init__(self, data):
        self.update_id = data['update_id']
        self.message = data.get('message', None)
        self.edited_message = data.get('edited_message', None)
        self.channel_post = data.get('channel_post', None)
        self.edited_channel_post = data.get('edited_channel_post', None)
        self.inline_query = data.get('inline_query', None)
        self.callback_query = data.get('callback_query', None)
        self.shipping_query = data.get('shipping_query', None)
        self.pre_checkout_query = data.get('pre_checkout_query', None)
        self.poll = data.get('poll', None)
        self.poll_answer = data.get('poll_answer', None)
