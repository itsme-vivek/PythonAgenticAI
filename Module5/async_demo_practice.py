import asyncio

async def download_data():
    print('Downloading...')
    await asyncio.sleep(2)
    print('Download Completed')
    
asyncio.run(download_data())

# Create Event Loop
#         │
#         ▼
# Create Coroutine
#         │
#         ▼
# Execute download_data()
#         │
#         ▼
# Downloading...
#         │
#         ▼
# await asyncio.sleep(2)
#         │
#         ▼
# Pause this coroutine
#         │
#         ▼
# Event Loop waits or runs other coroutines
#         │
#         ▼
# Resume download_data()
#         │
#         ▼
# Download Completed