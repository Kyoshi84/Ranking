
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
from crispy_forms.utils import render_field
from crispy_forms import layout as crispy_forms_layout
from crispy_forms.bootstrap import InlineField, FormActions, StrictButton


class ScrollListFormHelper(FormHelper):
    form_id = 'scroll-search-form'
    form_class = 'form-inline'
    field_template = 'bootstrap3/layout/inline_field.html'
    field_class = 'col-xs-3'
    label_class = 'col-xs-3'
    form_show_errors = True
    help_text_inline = False
    html5_required = True
    layout = Layout(
                Fieldset(
                    '<i class="fa fa-search"></i> Search Warscroll Records',
                    InlineField('scroll_id'),
                    InlineField('scroll_name'),
                    InlineField('scroll_army'),
                    InlineField('scroll_key'),
                ),
                FormActions(
                    StrictButton(
                        '<i class="fa fa-search"></i> Search',
                        type='submit',
                        css_class='btn-primary',
                        style='margin-top:10px;')
                )
    )
