async function get_fetch(url,method='GET',data=null){
    const host="http://127.0.0.1:8000/api/v1"
    headers={
        method:method
    }
    data!=null?headers['body']=JSON.stringify(data):""
    data!=null?headers["headers"]={ "Content-Type": "application/json"}:""
    res=await fetch(host+url,headers)
    if(!res.ok){
        return {'code':400,'message':"请求错误"}
    }
    return await res.json()
}