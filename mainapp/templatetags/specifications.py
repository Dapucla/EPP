from django import template
from django.utils.safestring import mark_safe

from mainapp.models import Smartphone


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                <tr>
                  <td>{name}</td>
                  <td>{value}</td>
                </tr>
                """

PRODUCT_SPEC = {
    'notebook': {
        'Диагональ': 'diagonal',
        'Тип дислея': 'display_type',
        'Частота процессора': 'processor_freq',
        'Оперативная память': 'ram',
        'Видеокарта': 'video',
        'Время работы аккумулятора': 'time_without_charge',
    },
    'smartphone': {
        'Диагональ': 'diagonal',
        'Тип дислея': 'display_type',
        'Разрешение экрана': 'resolution',
        'Заряд аккумулятора': 'accum_volume',
        'Оперативная память': 'ram',
        'Наличие слота для карты памяти': 'sd',
        'Максимальный объем SD карты': 'sd_volume_max',
        'Задняя Камера МП': 'main_cam_mp',
        'Фронтальная камера МП': 'frontal_cam_mp',
    },
    'headphones': {
        'Тип подключения': 'type_of_connection',
        'Система активного шумоподваления': 'active_noise_cancelling',
        'Время работы без подзярядки': 'time_without_charge',
        'Проводные/Беспроводные': 'wireless',
    },
    'smartwatches': {
        'Диагональ': 'diagonal',
        'Тип дислея': 'display_type',
        'Время работы без подзярядки': 'time_without_charge',
    },
    'tv': {
        'Диагональ': 'diagonal',
        'Тип дислея': 'display_type',
        'Наличие USB': 'USB',
        'Наличие Smart TV': 'smartTV'
    },
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter()
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, Smartphone):
        if not product.sd:
            PRODUCT_SPEC['smartphone'].pop('Максимальный объем SD карты')
        else:
            PRODUCT_SPEC['smartphone']['Максимальный объем SD карты'] = 'sd_volume_max'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)