from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view


@api_view(['GET'])
def remind_me(request):
    if request.method == 'GET':
        email = request.GET.get('email', None)
        mobile = request.GET.get('mobile', None)
        message = request.GET.get('message', None)
        date = request.GET.get('date', None)
        time = request.GET.get('time', None)
        # if org_id:
        #     try:
        #         org = Organisation.objects.get(pk=org_id)
        #     except(Organisation.DoesNotExist, ValueError, Organisation.MultipleObjectsReturned):
        #         return HttpResponse('{No Data Found, Please Enter Valid Org ID}')
        #     org_team = org.org_team.all().exclude(parent_team__isnull=False)
        #     return render(request, template_name='org_temp.html', context={'org': org, 'org_team': org_team})
        # else:
        #     org = Organisation.objects.all()
        #     serializer = OrganisationSerializer(org, many=True)
        #     return Response(serializer.data)