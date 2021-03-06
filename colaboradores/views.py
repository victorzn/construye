# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, Http404, HttpResponse
from django.template import RequestContext

def convertir_datos(data):
    lista = []
    cadena = ""
    for d in data:
        cadena = cadena + "'" + d.lower()[:14] + "(" + str(data[d]) + "%)', "
        lista.append(data[d])
    return lista, cadena
        
def index_colaborador(request):
    if request.user.is_authenticated():
        #data = {'Jhon': 12, 'Richard': 29, 'Fred': 35, 'Brian': 17, 'Peter': 7}
        data = {'IMPUESTO DE ALCABALA':31,
        'CECION DE DERECHOS ALCABALA INVERMET':2,
        'IMPUESTO VEHICULAR - INSOLUTO P.A':1.7,
        'R.G.T.':06,
        'ARBITRIOS - LIMPIEZA PUBLICA P.A':5,
        'A LOS JUEGOS: TRAGAMONEDAS':4,
        'IMPUESTO PREDIAL - INSOLUTO P.A':3,
        'FONDO DE COMPENSACION MUNICIPAL':2,
        'IMPUESTO VEHICULAR - INSOLUTO A.A.':1
        }
        lista, cadena = convertir_datos(data)
        javascript = """
        window.onload = function ()
        {
            var pie3 = new RGraph.Pie('pie3', """ + str(lista) + """);
            pie3.Set('chart.key', [""" + cadena + """ ]);
            if (!RGraph.isOld()) {
                pie3.Set('chart.key.interactive', true);
            }
            pie3.Set('chart.key.position', 'graph');
            pie3.Set('chart.key.position.x', 300);
            pie3.Set('chart.key.position.y', 20);
            pie3.Set('chart.key.rounded', true);
            
            pie3.Set('chart.shadow', true);
            pie3.Set('chart.shadow.offsetx', 0);
            pie3.Set('chart.shadow.offsety', 0);
            pie3.Set('chart.shadow.blur', 25);
            pie3.Set('chart.title', 'Pie with interactive key');
            pie3.Set('chart.strokestyle', 'white');
            pie3.Set('chart.linewidth', 3);
            RGraph.isOld    () ? pie3.Draw() : RGraph.Effects.Pie.RoundRobin(pie3, {radius: false});
        }
        """
        return render_to_response("colaboradores/index_colaborador.html", {"javascript": javascript, "user": request.user })
    else:
        return HttpResponseRedirect('../../')
        
def ver_mapa(request):
    #data = {'IMPUESTO DE ALCABALA':31,
    #'CECION DE DERECHOS ALCABALA INVERMET':2,
    #'IMPUESTO VEHICULAR - INSOLUTO P.A':1.7,
    #'R.G.T.':06,
    #'ARBITRIOS - LIMPIEZA PUBLICA P.A':5,
    #'A LOS JUEGOS: TRAGAMONEDAS':4,
    #'IMPUESTO PREDIAL - INSOLUTO P.A':3,
    #'FONDO DE COMPENSACION MUNICIPAL':2,
    #'IMPUESTO VEHICULAR - INSOLUTO A.A.':1
    #}
    #lista, cadena = convertir_datos(data)
    #javascript = """
    #window.onload = function ()
    #{
        #var pie3 = new RGraph.Pie('pie3', """ + str(lista) + """);
        #pie3.Set('chart.key', [""" + cadena + """ ]);
        #if (!RGraph.isOld()) {
            #pie3.Set('chart.key.interactive', true);
        #}
        #pie3.Set('chart.key.position', 'graph');
        #pie3.Set('chart.key.position.x', 300);
        #pie3.Set('chart.key.position.y', 20);
        #pie3.Set('chart.key.rounded', true);
        
        #pie3.Set('chart.shadow', true);
        #pie3.Set('chart.shadow.offsetx', 0);
        #pie3.Set('chart.shadow.offsety', 0);
        #pie3.Set('chart.shadow.blur', 25);
        #pie3.Set('chart.title', 'Pie with interactive key');
        #pie3.Set('chart.strokestyle', 'white');
        #pie3.Set('chart.linewidth', 3);
        #RGraph.isOld    () ? pie3.Draw() : RGraph.Effects.Pie.RoundRobin(pie3, {radius: false});
    #}
    #"""
    return render_to_response("colaboradores/mapas/mapa.html", {"user": request.user })

def ver_sugerencia(request):
    if request.user.is_authenticated():
        return render_to_response("colaboradores/mapas/sugerencia.html", {"user": request.user })
    else:
        return HttpResponseRedirect('../../')

def escribir_textfile(request):
    if request.user.is_authenticated():
        if request.method == 'POST':
            print request
            escribir('a','b','c')
        return render_to_response("colaboradores/mapas/sugerencia.html", {"user": request.user })
    else:
        return HttpResponseRedirect('../../')
        

def escribir(a,b,c):
    import os
    ruta_archivo1 = "/home/zonvi/projects/construye/static/media/mapquery/data/textfile.txt"
    #ruta_archivo2 = "/home/zchronos/Documentos/victor/textfile2.txt"

    linea_nueva = "%s\t%s\t%s\n" % (a,b,c)

    archivo = open(ruta_archivo1, 'wb+')
    #destination = open(ruta_archivo2, 'wb+')
    for linea in archivo.readlines():
        #destination.writelines(linea)
        pass
    destination.writelines(linea_nueva)
    destination.close()

def como_funciona(request):
    if request.user.is_authenticated():
        return render_to_response("colaboradores/como_funciona.html", {"user": request.user })
    else:
        return HttpResponseRedirect('../../')