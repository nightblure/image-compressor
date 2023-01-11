def get_url_by_route_name(router, name):
    route = router.get(name, None)
    if not route:
        raise Exception(f'Route with name {name} was not found!')
    return route.url_for()
