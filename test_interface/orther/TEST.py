def _requests(ss, data):
    url = data["URL"]
    method = data["请求方法"]
    params = data["请求参数"]
    headers = data["请求头"]
    bodydata = data["请求body"]
    # 判断传data数据还是json
    if data["参数类型"] == "data":
        body = bodydata
    elif data["参数类型"] == "json":
        body = json.dumps(bodydata)
        # body = json.loads(bodydata)
    else:
        body = bodydata
    result = ss.request(method=method,
                        url=url,
                        params=params,
                        headers=headers,
                        data=body,
                        verify=False
                        )
    return result