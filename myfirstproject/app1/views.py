from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect,Http404
from django.urls import reverse
from django.template.loader import render_to_string

# Create your views here.
# def jan(request):
#     return  HttpResponse("hello jay")

# def feb(request):
#     return HttpResponse("ok start new project")


months_data={
    'january':'hello',
    'february':'start you django project',
    'march':'all task done',
    'april':None
}


def index(request):
    # list_item=""
    # months=list(months_data.keys())

    # for month in months:
    #     capatilized_month=month.capitalize()
    #     month_path=reverse("month-challenges",args=[month])
    #     list_item += f"<li><a href=\"{month_path}\">{capatilized_month}</a></li>"
    # response_data=f"<ul>{list_item}</ul>"
    # return HttpResponse(response_data)

    months=list(months_data.keys())
    return render(request,"app1/index.html",{"months":months})


def monthsDataNuber(request,month):
    month_of_user=list(months_data.keys())
    if month>len(month_of_user):
        return HttpResponseNotFound("not valid month")
    challege_text=month_of_user[month - 1]
    rediret_path=reverse("month-challenges",args=[challege_text])#challenge/janauary
    # return HttpResponseRedirect("/challenge/"+challege_text)
    return HttpResponseRedirect(rediret_path)

    
        



    # challege_text=None
    # if month==1:
    #     challege_text='see django tutorial'
    # elif month==2:
    #     challege_text='complete your task'
    # else:
    #     return HttpResponseNotFound('this month number is not valid')
    # return HttpResponse(challege_text)


# def monthsData(request,month):
#     # challege_text=None
#     # if month=='january':
#     #     challege_text='see django tutorial api'
#     # elif month=='february':
#     #     challege_text='complete your task with token'
#     # else:
#     #     return HttpResponseNotFound('this month is not valid')
#     # return HttpResponse(challege_text)

#     # reduce code with use of dictionary
#     try:
#         challege_text=months_data[month]
#         new_html_response=f"<h1>{challege_text}</h1>"
#         return HttpResponse(new_html_response)
#     except:
#         return HttpResponseNotFound('<h1>this month not found</h1>')




# render html file data
def monthsData(request,month):

    try:
        challege_text=months_data[month]
        return render(request,"app1/challenge.html",{
            "text":challege_text,
            "month_name":month.capitalize()

        })
        # new_html_response=render_to_string("app1/challenge.html")
        # return HttpResponse(new_html_response)
    # except:
    #     return HttpResponseNotFound('<h1>this month not found</h1>')
    except:
        raise Http404()