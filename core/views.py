from django.shortcuts import render, HttpResponse


html_base = """
<H1>Mi web personal</H1>
<ul>
<li><a href="/">Portada</a></li>
<li><a href="/about-me/">Acerca de</a></li>
<li><a href="/portfolio/">Portafolio</a></li>
<li><a href="/contact/">Contacto</a></li>
<ul>

"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + """
    <H2>Portada</H2>
    <P>Esto es la portada</P>
    
    """)

def about(request):
    return HttpResponse(html_base + """
    <H2>Acerca de</H2> 
    <P>Me llamo Luis Angel Larios Castillo y soy programador.</P>
    
    """)

def portfolio(request):
    return HttpResponse(html_base + """
    <H2>Portafolio</H2> 
    <P>Estas en el portafolio de Luis Angel Larios Castillo</P>
    
    """)

def contact(request):
    return HttpResponse(html_base + """
    <H2>Contacto</H2> 
    <P>A que te dejo mi redes solicales para que me puedas contactar</P>
    <ul>
    <li><a href="">WhatsApp</a></li>
    <li><a href="">Facebook</a></li>
    <li><a href="">You Tube</a></li>
    </ul>
    
    """)