from datetime import date
from django.forms import widgets

VERSION = "1.1.3"


class DateOfBirthWidget(widgets.MultiWidget):
    
    def __init__(self, attrs=None, order=None, **kwargs):
        if order is None:
            order = 'DMY'
        order = tuple(order)
        if sorted(order) != sorted('DMY'):
            raise ValueError("You must provide an order string of either 'DMY', 'MDY' or 'YMD'")
        self.order = order

        child_attrs = {'type': 'number'}
        if attrs:
            child_attrs.update(attrs)

        day_attrs = {'placeholder': 'DD', 'min': 1, 'max': 31}
        day_attrs.update(child_attrs)
        if 'day_attrs' in kwargs:
            day_attrs.update(kwargs['day_attrs'])
        month_attrs = {'placeholder': 'MM', 'min': 1, 'max': 12}
        month_attrs.update(child_attrs)
        if 'month_attrs' in kwargs:
            month_attrs.update(kwargs['month_attrs'])
        year_attrs = {'placeholder': 'YYYY', 'min': 1, 'max': 9999}
        year_attrs.update(child_attrs)
        if 'year_attrs' in kwargs:
            year_attrs.update(kwargs['year_attrs'])
        
        subwidgets = {
            'D': widgets.TextInput(attrs=day_attrs),
            'M': widgets.TextInput(attrs=month_attrs),
            'Y': widgets.TextInput(attrs=year_attrs),
        }
        ordered_subwidgets = [subwidgets[key] for key in self.order]
        super(DateOfBirthWidget, self).__init__(ordered_subwidgets, attrs)

    def decompress(self, value):
        if value:
            value = {
                'D': value.day,
                'M': value.month,
                'Y': value.year,
            }
            return [value[key] for key in self.order]
        return [None, None, None]

    def format_output(self, rendered_widgets):
        return ''.join(rendered_widgets)

    def value_from_datadict(self, data, files, name):
        matched_widgets = zip(self.order, self.widgets)
        values = {}
        index = 0
        try:
            for key, widget in matched_widgets:
                value = widget.value_from_datadict(data, files, '{0}_{1}'.format(name, index))
                values[key] = int(value)
                index += 1
            return date(values['Y'], values['M'], values['D'])
        except (ValueError, TypeError, ArithmeticError):
            return super(DateOfBirthWidget, self).value_from_datadict(data, files, name)
