# Generated by Django 4.1.3 on 2023-06-14 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_recibopedido_fk_id_estado_pedido_fk_id_estado'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='estado_pedido',
        ),
    ]
