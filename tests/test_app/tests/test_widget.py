import datetime
from unittest import TestCase
from distutils.version import StrictVersion
import pytest
import django
from dobwidget import DateOfBirthWidget

from ..models import Person
from ..forms import PersonModelForm, DMYPersonModelForm, MDYPersonModelForm, YMDPersonModelForm


django_version = django.get_version()
is_gt_dj110 = StrictVersion(django_version) >= StrictVersion('1.10.0')


@pytest.mark.django_db
class SimpleTestCase(TestCase):
    
    def setUp(self):
        super(SimpleTestCase, self).setUp()
        self.person = Person(name="A person", date_of_birth=datetime.date(2000, 4, 4))

    def test_raw(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" required />'
        )
        form = PersonModelForm()
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_instance(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="4" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="4" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2000" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="4" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="4" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2000" required />'
        )
        form = PersonModelForm(instance=self.person)
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_POST(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="3" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="5" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="3" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="5" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" required />'
        )
        form = PersonModelForm({
            'name': 'Example',
            'date_of_birth_0': '3',
            'date_of_birth_1': '5',
            'date_of_birth_2': '2001',
        })
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['date_of_birth'], datetime.date(year=2001, month=5, day=3))
    

@pytest.mark.django_db
class DMYTestCase(SimpleTestCase):
    
    def test_raw(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" required />'
        )
        form = DMYPersonModelForm()
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_instance(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="4" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="4" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2000" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="4" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="4" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2000" required />'
        )
        form = DMYPersonModelForm(instance=self.person)
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_POST(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="3" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="5" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="3" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="5" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" required />'
        )
        form = DMYPersonModelForm({
            'name': 'Example',
            'date_of_birth_0': '3',
            'date_of_birth_1': '5',
            'date_of_birth_2': '2001',
        })
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['date_of_birth'], datetime.date(year=2001, month=5, day=3))


@pytest.mark.django_db
class MDYTestCase(SimpleTestCase):
    
    def test_raw(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="12" min="1" name="date_of_birth_0" placeholder="MM" type="number" />'
            u'<input id="id_date_of_birth_1" max="31" min="1" name="date_of_birth_1" placeholder="DD" type="number" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="12" min="1" name="date_of_birth_0" placeholder="MM" type="number" required />'
            u'<input id="id_date_of_birth_1" max="31" min="1" name="date_of_birth_1" placeholder="DD" type="number" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" required />'
        )
        form = MDYPersonModelForm()
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_instance(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="12" min="1" name="date_of_birth_0" placeholder="MM" type="number" value="4" />'
            u'<input id="id_date_of_birth_1" max="31" min="1" name="date_of_birth_1" placeholder="DD" type="number" value="4" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2000" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="12" min="1" name="date_of_birth_0" placeholder="MM" type="number" value="4" required />'
            u'<input id="id_date_of_birth_1" max="31" min="1" name="date_of_birth_1" placeholder="DD" type="number" value="4" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2000" required />'
        )
        form = MDYPersonModelForm(instance=self.person)
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_POST(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="12" min="1" name="date_of_birth_0" placeholder="MM" type="number" value="5" />'
            u'<input id="id_date_of_birth_1" max="31" min="1" name="date_of_birth_1" placeholder="DD" type="number" value="3" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="12" min="1" name="date_of_birth_0" placeholder="MM" type="number" value="5" required />'
            u'<input id="id_date_of_birth_1" max="31" min="1" name="date_of_birth_1" placeholder="DD" type="number" value="3" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" required />'
        )
        form = MDYPersonModelForm({
            'name': 'Example',
            'date_of_birth_0': '5',
            'date_of_birth_1': '3',
            'date_of_birth_2': '2001',
        })
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['date_of_birth'], datetime.date(year=2001, month=5, day=3))


@pytest.mark.django_db
class YMDTestCase(SimpleTestCase):
    
    def test_raw(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="9999" min="1" name="date_of_birth_0" placeholder="YYYY" type="number" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" />'
            u'<input id="id_date_of_birth_2" max="31" min="1" name="date_of_birth_2" placeholder="DD" type="number" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="9999" min="1" name="date_of_birth_0" placeholder="YYYY" type="number" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" required />'
            u'<input id="id_date_of_birth_2" max="31" min="1" name="date_of_birth_2" placeholder="DD" type="number" required />'
        )
        form = YMDPersonModelForm()
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_instance(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="9999" min="1" name="date_of_birth_0" placeholder="YYYY" type="number" value="2000" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="4" />'
            u'<input id="id_date_of_birth_2" max="31" min="1" name="date_of_birth_2" placeholder="DD" type="number" value="4" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="9999" min="1" name="date_of_birth_0" placeholder="YYYY" type="number" value="2000" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="4" required />'
            u'<input id="id_date_of_birth_2" max="31" min="1" name="date_of_birth_2" placeholder="DD" type="number" value="4" required />'
        )
        form = YMDPersonModelForm(instance=self.person)
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_POST(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="9999" min="1" name="date_of_birth_0" placeholder="YYYY" type="number" value="2001" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="5" />'
            u'<input id="id_date_of_birth_2" max="31" min="1" name="date_of_birth_2" placeholder="DD" type="number" value="3" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="9999" min="1" name="date_of_birth_0" placeholder="YYYY" type="number" value="2001" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="5" required />'
            u'<input id="id_date_of_birth_2" max="31" min="1" name="date_of_birth_2" placeholder="DD" type="number" value="3" required />'
        )
        form = YMDPersonModelForm({
            'name': 'Example',
            'date_of_birth_0': '2001',
            'date_of_birth_1': '5',
            'date_of_birth_2': '3',
        })
        field = form['date_of_birth']
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )
        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['date_of_birth'], datetime.date(year=2001, month=5, day=3))
    

class BadOptionsTestCase(TestCase):
    
    def test_duplicate_order_elements_disallowed(self):
        with pytest.raises(ValueError):
            DateOfBirthWidget(order='YYMD')
            DateOfBirthWidget(order='YYD')

    def test_invalid_options_disallowed(self):
        with pytest.raises(ValueError):
            DateOfBirthWidget(order='YMZ')

    def test_lowercase_disallowed(self):
        with pytest.raises(ValueError):
            DateOfBirthWidget(order='Ymd')

    def test_partial_options_disallowed(self):
        with pytest.raises(ValueError):
            DateOfBirthWidget(order='YM')


class InvalidInputTestCase(TestCase):
    
    def test_single_invalid_input_is_equivalent_to_raw_text_inputs_but_invalid(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="a" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="b" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="a" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="b" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" required />'
        )
        form = PersonModelForm({
            'name': 'Example',
            'date_of_birth_0': 'a',
            'date_of_birth_1': 'b',
            'date_of_birth_2': '2001',
        })
        field = form['date_of_birth']
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors)
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_invalid_month_is_equivalent_to_raw_text_inputs_but_invalid(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="1" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="14" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="1" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="14" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" required />'
        )
        form = PersonModelForm({
            'name': 'Example',
            'date_of_birth_0': '1',
            'date_of_birth_1': '14',
            'date_of_birth_2': '2001',
        })
        field = form['date_of_birth']
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors)
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_invalid_date_is_equivalent_to_raw_text_inputs_but_invalid(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="29" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="2" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="29" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="2" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="2001" required />'
        )
        form = PersonModelForm({
            'name': 'Example',
            'date_of_birth_0': '29',
            'date_of_birth_1': '2',
            'date_of_birth_2': '2001',
        })
        field = form['date_of_birth']
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors)
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )

    def test_invalid_date_far_future_is_equivalent_to_raw_text_inputs_but_invalid(self):
        expected_lt_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="21" />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="2" />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="198000000000000" />'
        )
        expected_gte_dj110 = (
            u'<input id="id_date_of_birth_0" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" value="21" required />'
            u'<input id="id_date_of_birth_1" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" value="2" required />'
            u'<input id="id_date_of_birth_2" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" value="198000000000000" required />'
        )
        form = PersonModelForm({
            'name': 'Example',
            'date_of_birth_0': '21',
            'date_of_birth_1': '2',
            'date_of_birth_2': '198000000000000',
        })
        field = form['date_of_birth']
        self.assertFalse(form.is_valid())
        self.assertIn('date_of_birth', form.errors)
        self.assertEqual(
            field.as_widget(),
            expected_gte_dj110 if is_gt_dj110 else expected_lt_dj110
        )


class AttributesTestCase(TestCase):

    def test_attrs_can_be_specified_per_field(self):
        widget = DateOfBirthWidget(
            attrs={'data-foo': 'bar'},
            day_attrs={'data-type': 'day'},
            month_attrs={'data-type': 'month'},
            year_attrs={'data-type': 'year'},
        )
        self.assertEqual(
            widget.render('date_of_birth', None),
            u'<input data-foo="bar" data-type="day" max="31" min="1" name="date_of_birth_0" placeholder="DD" type="number" />'
            u'<input data-foo="bar" data-type="month" max="12" min="1" name="date_of_birth_1" placeholder="MM" type="number" />'
            u'<input data-foo="bar" data-type="year" max="9999" min="1" name="date_of_birth_2" placeholder="YYYY" type="number" />'
        )
