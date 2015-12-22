from django.contrib.syndication.views import Feed
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from blogango.models import Blog, BlogEntry
from taggit.models import Tag


class main_feed(Feed):
    blog = Blog.objects.get_blog()
    if blog:
        title = blog.title
        link = "/rss/latest/"
        description = blog.tag_line

    def items(self):
        return BlogEntry.objects.filter(is_page=False)[:10]

    def item_description(self, item):
        # print self.request

        return item.text_with_abs_url(request=self.request)

    def get_context_data(self, **kwargs):
        # print 'get_context_data',kwargs
        context = super(main_feed, self).get_context_data(**kwargs)
        self.request = kwargs.get('request',{})
        return context

class CatFeed(Feed):
    def get_object(self, request, tag):
        return get_object_or_404(Tag, name=tag)

    def title(self, obj):
        return "%s" % obj.name

    def link(self, obj):
        if not obj:
            raise ObjectDoesNotExist
        return reverse('blogango_tag_details', args=[obj.slug])

    def description(self, obj):
        return "Category: %s" % obj.name

    def items(self, obj):
        return BlogEntry.objects.filter(tags__in=[obj], is_page=False)

    def item_description(self, obj):
        return obj.text
