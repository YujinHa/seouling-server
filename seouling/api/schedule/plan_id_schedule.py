from rest_framework.views import APIView
from rest_framework.response import Response
from api.schedule.serializer import ScheduleSerializer
from django.core.paginator import Paginator
from utils.page_serializer import PageSerializer
from api.models import Schedule


class PlanScheduleView(APIView):

    def get(self, request, plan_id):
        page = request.query_params.get('page', 1)

        schedule_query = Schedule.objects.filter(plan_id=plan_id).order_by('date')

        paginator = Paginator(schedule_query, 10)
        page = paginator.page(page)

        result = dict()
        result['data'] = ScheduleSerializer(page.object_list, many=True).data
        result['paging'] = PageSerializer(page, context={'request': request}).data

        return Response(status=200, data=result)
