from django.core.cache import cache

from common import keys


# 自定义装饰器实现缓存操作
def page_cache(timeou):
    def warp1(view_func):
        def warp2(request):
            key = keys.PAGE_CACHE_KEY %(request.session.session_key, request.get_full_path())
            print('key is %s' %key)
            response = cache.get(key)
            if response is  None:
                response = view_func(request)
                cache.set(key, response, timeou)
            return response
        return warp2
    return warp1
