#rymme






from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
    return web.json_response("BOT IS RUNNING -https://www.instagram.com/iammoneyangel?igsh=MWNmODNqaW15bGw4Zw==")
