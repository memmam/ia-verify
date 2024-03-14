from internetarchive import get_session, get_item

# s = ArchiveSession()
s = get_session()
s.mount_http_adapter()
search_results = s.search_items('kD9NUhMg2Eg')
for result in search_results:
    print(result['identifier'])
    id = result['identifier']
    item = get_item(id)
    print(item.metadata)
    # print(result)
# print(search_results)
