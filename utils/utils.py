from xhtml2pdf import pisa
from django.template.loader import get_template
from django.http import HttpResponse
from html import escape
import io


def render_to_pdf(template_src, context_dict):
    template = get_template(template_src)
    context = context_dict
    html = template.render(context)
    result = io.BytesIO()

    pdf = pisa.pisaDocument(
        io.BytesIO(html.encode("UTF-8")),
        dest=result)
    if not pdf.err:
        return HttpResponse(result.getvalue(), content_type='application/pdf')
    return HttpResponse('We had some errors<pre>%s</pre>' % escape(html))
