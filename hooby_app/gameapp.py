from django.shortcuts import redirect,render
from django.http import JsonResponse
import json
import pusher
from django.views.decorators.csrf import csrf_exempt
from django.http.response import HttpResponse

pusher = pusher_client = pusher.Pusher(
  app_id='934602',
  key='5d68ac6ac406e5d01004',
  secret='a84a1b7020a7f60baac1',
  cluster='ap2',
  ssl=True
)
name=''

def index(request):

  return render(request, 'game/index.html')
@csrf_exempt
def play(request):
  global name
  name=request.user.username  
  return render(request,'game/play.html')

@csrf_exempt
def pusher_authentication(request):
  auth=pusher.authenticate(
    channel=request.POST['channel_name'],
    socket_id=request.POST['socket_id'],
    custom_data={
      u'user_id':name,
      u'user_info':{
        u'role':u'player'
      }
    }
  )  
  return JsonResponse(auth)

name = ''
