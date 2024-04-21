import json
from channels.generic.websocket import AsyncWebsocketConsumer

class LeadNotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.group_name = 'leads_group'
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )

    async def lead_notification(self, event):
        lead_data = event['lead_data']
        await self.send(text_data=json.dumps(lead_data))
