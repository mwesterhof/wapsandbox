from wagtail.core import blocks


class OverviewBlock(blocks.StructBlock):
    title = blocks.CharBlock()

    class Meta:
        template = 'news/blocks/overview.html'
