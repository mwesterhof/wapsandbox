# Generated by Django 2.0.4 on 2018-04-16 16:03

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields
import wagtail_app_pages.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailtrans', '0007_auto_20180327_1127'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products', to='products.Category')),
            ],
        ),
        migrations.CreateModel(
            name='ProductPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='wagtailcore.Page')),
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('pop_content', wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock())))),))),
                ('pdp_content', wagtail.core.fields.StreamField((('paragraph', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock()), ('body', wagtail.core.blocks.TextBlock())))), ('order_product_cta', wagtail.core.blocks.StructBlock((('title', wagtail.core.blocks.CharBlock(help_text='Use $product to refer to the product name')), ('body', wagtail.core.blocks.TextBlock(help_text='Use $product to refer to the product name')), ('cta_text', wagtail.core.blocks.CharBlock(help_text='Use $product to refer to the product name')))))))),
            ],
            options={
                'abstract': False,
            },
            bases=(wagtail_app_pages.models.AppPageMixin, 'wagtailtrans.translatablepage', 'wagtailcore.page'),
        ),
    ]