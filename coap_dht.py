import Adafruit_DHT
from aiocoap import *
from aiocoap import resource
import asyncio
import logging

logging.basicConfig(level=logging.INFO)

class DHTResource(resource.Resource):
    async def render_get(self, request):
        # Read data from DHT11 sensor on GPIO 4
        humidity, temperature = Adafruit_DHT.read_retry(Adafruit_DHT.DHT11, 4)
        if humidity is not None and temperature is not None:
            payload = 'Temperature: {:.1f} C, Humidity: {:.1f} %'.format(temperature, humidity)
        else:
            payload = 'Failed to read data from sensor'
        return Message(payload=payload.encode('utf-8'))

async def main():
    # Create CoAP context and bind to interface
    context = await Context.create_server_context(DHTResource())

    logging.info('CoAP server started on [::]:5683')

    # Keep running until the program is interrupted
    await asyncio.gather(
        asyncio.Event().wait()
    )

if __name__ == "__main__":
    asyncio.run(main())

