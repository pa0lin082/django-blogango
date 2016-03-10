# -*- coding: utf-8 -*-
from django.contrib.syndication.views import Feed
from django.utils.feedgenerator import Rss201rev2Feed, SimplerXMLGenerator
from xml.sax.saxutils import escape
from django.core.urlresolvers import reverse
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import get_object_or_404

from blogango.models import Blog, BlogEntry, BlogCategory
from taggit.models import Tag


class MySimplerXMLGenerator(SimplerXMLGenerator):
    pass
    def addQuickElement(self, name, contents=None, attrs=None, escaped=True):
        "Convenience method for adding an element with no children"
        if attrs is None: attrs = {}
        self.startElement(name, attrs)
        if contents is not None:
            self.characters(contents, escaped=escaped)
        self.endElement(name)

    def characters(self, content, escaped=True):
        # print 'characters: ',escaped, content
        if not isinstance(content, unicode):
            content = unicode(content, self._encoding)
        if escaped:
            self._write(escape(content))
        else:
            self._write(content)


class MyRssFeedGenerator(Rss201rev2Feed):
    mime_type = 'text/xml; charset=utf-8'


    def write(self, outfile, encoding):
        handler = MySimplerXMLGenerator(outfile, encoding)
        handler.startDocument()
        handler.startElement("rss", self.rss_attributes())
        handler.startElement("channel", self.root_attributes())
        self.add_root_elements(handler)
        self.write_items(handler)
        self.endChannelElement(handler)
        handler.endElement("rss")

    def rss_attributes(self):
        attrs = super(MyRssFeedGenerator, self).rss_attributes()
        attrs['xmlns:content'] = 'http://purl.org/rss/1.0/modules/content/'
        attrs['xmlns:media'] = 'http://search.yahoo.com/mrss/'
        return attrs

    def add_item_elements(self, handler, item):
        super(MyRssFeedGenerator, self).add_item_elements(handler, item)
        if item.has_key('content_encoded') and item['content_encoded'] is not None:
            # handler.addQuickElement("content:encoded", item['content:encoded'])
            handler.addQuickElement(u'content:encoded', item['content_encoded'], escaped=False)
        if item.has_key('media_content') and item['media_content'] is not None:
            # handler.addQuickElement("media:content", item['media_content'])
            handler.addQuickElement(u'media:content', '', {"url": item['media_content'], "medium":"image"})


class main_feed(Feed):
    feed_type = MyRssFeedGenerator

    blog = Blog.objects.get_blog()
    if blog:
        title = blog.title
        link = "/rss/latest/"
        description = blog.tag_line

    # def item_extra_kwargs(self, item):
    #     """
    #     Returns an extra keyword arguments dictionary that is used with
    #     the `add_item` call of the feed generator.
    #     """
    #     content_encoded = item.text_with_abs_url(request=self.request)
    #
    #     return {
    #         # 'content:encoded': content_encoded
    #     }

    def item_enclosure_url(self, item):
        return item.preview_image(width=400, height=None, request=self.request, absolute=True)

    def item_categories(self,item):
        if item.category:
            return ("<![CDATA[%s]]>" % item.category.title,)
        else:
            return None

    def item_extra_kwargs(self, item):
        return {
            'content_encoded': self.item_content_encoded(item),
            'media_content': self.item_media_content(item),
            # 'author_name': self.item_author_name(item)
        }

    def item_media_content(self, item):
        # return 'foo'
        return item.preview_image(width=800, height=None, request=self.request, absolute=True)

    def item_content_encoded(self, item):
        # return 'content_encoded'
        # return item.text_with_abs_url(request=self.request)
        return "<![CDATA[%s]]>" % item.text_with_abs_url(request=self.request)

    def items(self):
        return BlogEntry.objects.filter(is_page=False)[:10]

    def item_author_name(self, item):
        return u'Manabú'

    def item_pubdate(self, item):
        return item.publish_date

    def item_description(self, item):
        # print self.request
        return item.meta_description
        # return 'desc'
        # return item.text_with_abs_url(request=self.request)
        # return "<![CDATA[%s]]>" % item.text_with_abs_url(request=self.request)
        # return "<![CDATA[%s]]>" % item.meta_description

    def get_context_data(self, **kwargs):
        # print 'get_context_data',kwargs
        context = super(main_feed, self).get_context_data(**kwargs)
        self.request = kwargs.get('request', {})
        return context


class CatFeed(main_feed):
    def get_object(self, request, tag):
        return get_object_or_404(BlogCategory, slug=tag)

    def title(self, obj):
        return "%s" % obj.title

    def link(self, obj):
        if not obj:
            raise ObjectDoesNotExist
        return reverse('blogango_tag_details', args=[obj.slug])

    def description(self, obj):
        return "Category: %s" % obj.title

    def items(self, obj):
        return BlogEntry.objects.filter(category__in=[obj], is_page=False)

    def item_description(self, obj):
        return obj.text
