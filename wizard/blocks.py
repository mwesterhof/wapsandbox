from wagtail.core import blocks


class CharFieldBlock(blocks.StructBlock):
    name = blocks.CharBlock()
    placeholder = blocks.CharBlock()
